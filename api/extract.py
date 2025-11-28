"""
API Serverless para extração de EAN/GTIN
Compatível com Vercel Serverless Functions
"""

import json
import requests
from bs4 import BeautifulSoup
import re
from typing import Dict, Optional

def handler(request):
    """
    Handler para Vercel Serverless Function
    """
    # Headers CORS
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    # Handle OPTIONS (CORS preflight)
    method = getattr(request, 'method', 'GET')
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': headers,
            'body': ''
        }
    
    try:
        # Obter dados da requisição
        if method == 'POST':
            try:
                body_str = getattr(request, 'body', '{}')
                if isinstance(body_str, str):
                    body = json.loads(body_str)
                elif hasattr(request, 'json'):
                    body = request.json
                else:
                    body = {}
            except:
                body = {}
            urls = body.get('urls', [])
        else:
            # GET request
            urls = []
        
        if not urls:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Nenhuma URL fornecida'}, ensure_ascii=False)
            }
        
        # Processar URLs (limitar a 10 por vez para evitar timeout)
        urls = urls[:10]
        results = []
        for url in urls:
            result = get_ean_and_title(url)
            results.append({
                'url': url,
                **result
            })
        
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'results': results,
                'total': len(results),
                'success': sum(1 for r in results if r['status'] == '✅')
            }, ensure_ascii=False)
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({'error': str(e)}, ensure_ascii=False)
        }


def get_ean_and_title(url: str) -> Dict[str, Optional[str]]:
    """
    Extrai o código EAN/GTIN e título do produto de uma URL do Mercado Livre.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://www.google.com/'
    }
    
    result = {
        'ean': None,
        'title': None,
        'status': '❌'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Buscar EAN no JSON-LD
        scripts = soup.find_all('script', type='application/ld+json')
        for script in scripts:
            if script.string:
                try:
                    data = json.loads(script.string)
                    if isinstance(data, list):
                        data = data[0]
                    
                    ean = (data.get('gtin13') or 
                          data.get('gtin') or 
                          data.get('isbn') or
                          data.get('mpn'))
                    
                    if ean:
                        result['ean'] = str(ean)
                        result['status'] = '✅'
                    
                    if not result['title']:
                        result['title'] = data.get('name')
                except json.JSONDecodeError:
                    continue
        
        # Extrair título do HTML
        if not result['title']:
            title_tag = soup.find('h1', class_='ui-pdp-title')
            if title_tag:
                result['title'] = title_tag.get_text(strip=True)
            else:
                meta_title = soup.find('meta', property='og:title')
                if meta_title:
                    result['title'] = meta_title.get('content')
        
        # Buscar EAN em scripts JavaScript
        if not result['ean']:
            scripts_text = soup.find_all('script')
            for script in scripts_text:
                if script.string and '__PRELOADED_STATE__' in script.string:
                    try:
                        ean_pattern = r'"gtin[13]?":\s*"(\d+)"|"ean":\s*"(\d+)"'
                        matches = re.findall(ean_pattern, script.string)
                        if matches:
                            for match in matches:
                                ean_candidate = match[0] or match[1]
                                if len(ean_candidate) >= 8:
                                    result['ean'] = ean_candidate
                                    result['status'] = '✅'
                                    break
                    except:
                        continue
        
    except requests.exceptions.Timeout:
        result['status'] = '⏱️ Timeout'
    except requests.exceptions.RequestException as e:
        result['status'] = f'❌ Erro: {str(e)[:30]}'
    except Exception as e:
        result['status'] = f'❌ Erro: {str(e)[:30]}'
    
    return result
