"""
API Serverless para extração de EAN/GTIN
Vercel Python Runtime
"""

import json
import requests
from bs4 import BeautifulSoup
import re

def handler(request):
    """Handler para Vercel Python Serverless Function"""
    
    # Headers CORS
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    try:
        # Método HTTP
        method = getattr(request, 'method', 'GET')
        
        # CORS preflight
        if method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': ''
            }
        
        # Obter URLs do body
        urls = []
        if method == 'POST':
            try:
                body = getattr(request, 'body', '{}')
                if isinstance(body, bytes):
                    body = body.decode('utf-8')
                if body:
                    data = json.loads(body)
                    urls = data.get('urls', [])
            except:
                pass
        
        if not urls:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Nenhuma URL fornecida'}, ensure_ascii=False)
            }
        
        # Processar URLs (máximo 10)
        results = []
        for url in urls[:10]:
            try:
                result = extract_ean(url)
                results.append({
                    'url': url,
                    'ean': result.get('ean'),
                    'title': result.get('title'),
                    'status': result.get('status', '❌')
                })
            except Exception as e:
                results.append({
                    'url': url,
                    'ean': None,
                    'title': None,
                    'status': f'❌ Erro'
                })
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'results': results,
                'total': len(results),
                'success': sum(1 for r in results if r.get('status') == '✅')
            }, ensure_ascii=False)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)}, ensure_ascii=False)
        }


def extract_ean(url):
    """Extrai EAN/GTIN de uma URL do Mercado Livre"""
    result = {'ean': None, 'title': None, 'status': '❌'}
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9',
            'Referer': 'https://www.google.com/'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Buscar em JSON-LD
        for script in soup.find_all('script', type='application/ld+json'):
            if script.string:
                try:
                    data = json.loads(script.string)
                    if isinstance(data, list):
                        data = data[0]
                    
                    ean = data.get('gtin13') or data.get('gtin') or data.get('isbn')
                    if ean:
                        result['ean'] = str(ean)
                        result['status'] = '✅'
                    
                    if not result['title']:
                        result['title'] = data.get('name')
                except:
                    continue
        
        # Título do HTML
        if not result['title']:
            title_tag = soup.find('h1', class_='ui-pdp-title')
            if title_tag:
                result['title'] = title_tag.get_text(strip=True)
        
        # EAN em scripts
        if not result['ean']:
            for script in soup.find_all('script'):
                if script.string and '__PRELOADED_STATE__' in script.string:
                    matches = re.findall(r'"gtin[13]?":\s*"(\d+)"|"ean":\s*"(\d+)"', script.string)
                    if matches:
                        ean_candidate = matches[0][0] or matches[0][1]
                        if len(ean_candidate) >= 8:
                            result['ean'] = ean_candidate
                            result['status'] = '✅'
                            break
        
    except requests.exceptions.Timeout:
        result['status'] = '⏱️ Timeout'
    except Exception as e:
        result['status'] = f'❌ Erro'
    
    return result
