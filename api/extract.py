"""
API Serverless para extração de EAN/GTIN
Compatível com Vercel Serverless Functions Python
"""

import json
import requests
from bs4 import BeautifulSoup
import re

def handler(request):
    """
    Handler para Vercel Serverless Function Python
    """
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    try:
        # Obter método
        method = getattr(request, 'method', 'GET')
        
        # CORS preflight
        if method == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': ''
            }
        
        # Obter body
        urls = []
        if method == 'POST':
            try:
                body_str = getattr(request, 'body', '{}')
                if isinstance(body_str, bytes):
                    body_str = body_str.decode('utf-8')
                if body_str:
                    body = json.loads(body_str)
                    urls = body.get('urls', [])
            except:
                urls = []
        
        if not urls:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Nenhuma URL fornecida'}, ensure_ascii=False)
            }
        
        # Processar URLs
        urls = urls[:10]  # Limitar a 10
        results = []
        for url in urls:
            try:
                result = get_ean_and_title(url)
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
                    'status': f'❌ Erro: {str(e)[:30]}'
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


def get_ean_and_title(url):
    """Extrai EAN/GTIN e título do produto"""
    result = {'ean': None, 'title': None, 'status': '❌'}
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9',
            'Referer': 'https://www.google.com/'
        }
        
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Buscar EAN no JSON-LD
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
                        for match in matches:
                            ean_candidate = match[0] or match[1]
                            if len(ean_candidate) >= 8:
                                result['ean'] = ean_candidate
                                result['status'] = '✅'
                                break
        
    except requests.exceptions.Timeout:
        result['status'] = '⏱️ Timeout'
    except Exception as e:
        result['status'] = f'❌ Erro: {str(e)[:30]}'
    
    return result
