import json
import requests
from bs4 import BeautifulSoup
import re

def handler(request):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    try:
        method = getattr(request, 'method', 'GET')
        
        if method == 'OPTIONS':
            return {'statusCode': 200, 'headers': headers, 'body': ''}
        
        urls = []
        if method == 'POST':
            try:
                body = getattr(request, 'body', b'{}')
                if isinstance(body, bytes):
                    body = body.decode('utf-8')
                data = json.loads(body) if body else {}
                urls = data.get('urls', [])
            except:
                urls = []
        
        if not urls:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({'error': 'Nenhuma URL fornecida'})
            }
        
        results = []
        for url in urls[:10]:
            try:
                ean, title, status = extract_data(url)
                results.append({
                    'url': url,
                    'ean': ean,
                    'title': title,
                    'status': status
                })
            except:
                results.append({
                    'url': url,
                    'ean': None,
                    'title': None,
                    'status': '❌'
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
            'body': json.dumps({'error': str(e)})
        }


def extract_data(url):
    ean = None
    title = None
    status = '❌'
    
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
        
        # JSON-LD
        for script in soup.find_all('script', type='application/ld+json'):
            if script.string:
                try:
                    data = json.loads(script.string)
                    if isinstance(data, list):
                        data = data[0]
                    ean = data.get('gtin13') or data.get('gtin') or data.get('isbn')
                    if ean:
                        ean = str(ean)
                        status = '✅'
                    if not title:
                        title = data.get('name')
                except:
                    continue
        
        # Título HTML
        if not title:
            title_tag = soup.find('h1', class_='ui-pdp-title')
            if title_tag:
                title = title_tag.get_text(strip=True)
        
        # EAN em scripts
        if not ean:
            for script in soup.find_all('script'):
                if script.string and '__PRELOADED_STATE__' in script.string:
                    matches = re.findall(r'"gtin[13]?":\s*"(\d+)"|"ean":\s*"(\d+)"', script.string)
                    if matches:
                        ean = matches[0][0] or matches[0][1]
                        if len(ean) >= 8:
                            status = '✅'
                            break
    except:
        status = '❌'
    
    return ean, title, status
