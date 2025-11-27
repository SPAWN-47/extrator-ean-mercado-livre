import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
import time
import random
import pandas as pd
from io import StringIO
from typing import Optional, Dict, List
import re

# Configuração da página
st.set_page_config(
    page_title="Extrator de EAN/GTIN - Mercado Livre",
    page_icon="🛒",
    layout="wide"
)

# Título e descrição
st.title("🛒 Extrator de EAN/GTIN - Mercado Livre")
st.markdown("""
**Extraia códigos EAN/GTIN em massa de produtos do Mercado Livre**
- Cole uma lista de URLs (uma por linha)
- O sistema processará cada URL e extrairá o código EAN do JSON-LD
- Resultados podem ser exportados em CSV
""")

# Função para extrair EAN/GTIN
def get_ean_and_title(url: str) -> Dict[str, Optional[str]]:
    """
    Extrai o código EAN/GTIN e título do produto de uma URL do Mercado Livre.
    
    Returns:
        Dict com 'ean', 'title' e 'status'
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
                    
                    # Tentar diferentes campos para EAN
                    ean = (data.get('gtin13') or 
                          data.get('gtin') or 
                          data.get('isbn') or
                          data.get('mpn'))
                    
                    if ean:
                        result['ean'] = str(ean)
                        result['status'] = '✅'
                    
                    # Extrair título
                    if not result['title']:
                        result['title'] = data.get('name')
                except json.JSONDecodeError:
                    continue
        
        # Se não encontrou no JSON-LD, tentar extrair título do HTML
        if not result['title']:
            title_tag = soup.find('h1', class_='ui-pdp-title')
            if title_tag:
                result['title'] = title_tag.get_text(strip=True)
            else:
                # Tentar meta tag
                meta_title = soup.find('meta', property='og:title')
                if meta_title:
                    result['title'] = meta_title.get('content')
        
        # Buscar EAN em outros lugares (script window.__PRELOADED_STATE__)
        if not result['ean']:
            scripts_text = soup.find_all('script')
            for script in scripts_text:
                if script.string and '__PRELOADED_STATE__' in script.string:
                    # Tentar extrair EAN do estado pré-carregado
                    try:
                        # Buscar padrão de EAN/GTIN no texto
                        ean_pattern = r'"gtin[13]?":\s*"(\d+)"|"ean":\s*"(\d+)"'
                        matches = re.findall(ean_pattern, script.string)
                        if matches:
                            for match in matches:
                                ean_candidate = match[0] or match[1]
                                if len(ean_candidate) >= 8:  # EAN válido tem pelo menos 8 dígitos
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

# Interface principal
urls_input = st.text_area(
    "📋 Cole as URLs do Mercado Livre (uma por linha):",
    height=200,
    placeholder="https://produto.mercadolivre.com.br/MLB-1234567890\nhttps://produto.mercadolivre.com.br/MLB-0987654321\n..."
)

# Botão de processamento
if st.button("🚀 Extrair Dados", type="primary", use_container_width=True):
    if not urls_input.strip():
        st.warning("⚠️ Por favor, cole pelo menos uma URL.")
    else:
        # Processar URLs
        urls = [url.strip() for url in urls_input.strip().split('\n') if url.strip()]
        
        if not urls:
            st.warning("⚠️ Nenhuma URL válida encontrada.")
        else:
            st.info(f"📊 Processando {len(urls)} URL(s)...")
            
            # Inicializar DataFrame para resultados
            results = []
            
            # Barra de progresso
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Container para tabela em tempo real
            results_container = st.empty()
            
            # Processar cada URL
            for idx, url in enumerate(urls):
                # Atualizar progresso
                progress = (idx + 1) / len(urls)
                progress_bar.progress(progress)
                status_text.text(f"🔄 Processando {idx + 1}/{len(urls)}: {url[:60]}...")
                
                # Extrair dados
                data = get_ean_and_title(url)
                
                # Adicionar resultado
                results.append({
                    'Status': data['status'],
                    'EAN/GTIN': data['ean'] or 'Não encontrado',
                    'Título': data['title'] or 'Não encontrado',
                    'URL': url
                })
                
                # Atualizar tabela em tempo real
                df_results = pd.DataFrame(results)
                results_container.dataframe(
                    df_results,
                    use_container_width=True,
                    hide_index=True
                )
                
                # Delay aleatório entre requisições (0.5 a 2 segundos)
                if idx < len(urls) - 1:  # Não esperar após a última URL
                    delay = random.uniform(0.5, 2.0)
                    time.sleep(delay)
            
            # Finalizar
            progress_bar.progress(1.0)
            status_text.text(f"✅ Processamento concluído! {len(results)} URL(s) processada(s).")
            
            # Armazenar resultados na sessão
            st.session_state['results_df'] = pd.DataFrame(results)
            st.session_state['results'] = results
            
            # Estatísticas
            success_count = sum(1 for r in results if r['Status'] == '✅')
            st.success(f"✅ {success_count} EAN(s) extraído(s) com sucesso de {len(results)} URL(s)!")

# Mostrar resultados salvos se existirem
if 'results_df' in st.session_state and not st.session_state['results_df'].empty:
    st.divider()
    st.subheader("📊 Resultados Finais")
    st.dataframe(
        st.session_state['results_df'],
        use_container_width=True,
        hide_index=True
    )
    
    # Botão de exportação CSV
    csv_buffer = StringIO()
    st.session_state['results_df'].to_csv(csv_buffer, index=False, encoding='utf-8-sig')
    csv_data = csv_buffer.getvalue()
    
    st.download_button(
        label="📥 Baixar CSV",
        data=csv_data,
        file_name=f"ean_extraction_{int(time.time())}.csv",
        mime="text/csv",
        use_container_width=True,
        type="primary"
    )
    
    # Estatísticas finais
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de URLs", len(st.session_state['results_df']))
    with col2:
        success = len(st.session_state['results_df'][st.session_state['results_df']['Status'] == '✅'])
        st.metric("Sucessos", success)
    with col3:
        failed = len(st.session_state['results_df'][st.session_state['results_df']['Status'] != '✅'])
        st.metric("Falhas", failed)

# Rodapé
st.divider()
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>Desenvolvido com ❤️ usando Streamlit | Extração de EAN/GTIN do Mercado Livre</small>
</div>
""", unsafe_allow_html=True)

