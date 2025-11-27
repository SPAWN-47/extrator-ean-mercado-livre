#!/bin/bash
# Script para executar o aplicativo Streamlit

cd "$(dirname "$0")"

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Erro: Ambiente virtual não encontrado!"
    echo "Execute primeiro: python3 -m venv venv"
    exit 1
fi

# Ativar ambiente virtual
source venv/bin/activate

# Verificar se o Streamlit está instalado
if ! command -v streamlit &> /dev/null; then
    echo "❌ Erro: Streamlit não está instalado!"
    echo "Execute: pip install streamlit"
    exit 1
fi

# Executar o Streamlit com opções explícitas
echo "🚀 Iniciando aplicativo Streamlit..."
echo "📱 O aplicativo abrirá em: http://localhost:8501"
echo ""
streamlit run app.py --server.port 8501 --server.address localhost


