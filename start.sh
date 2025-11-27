#!/bin/bash
# Script alternativo para iniciar o Streamlit com mais informações de debug

cd "$(dirname "$0")"

echo "🔍 Verificando ambiente..."
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado!"
    exit 1
fi
echo "✅ Python3 encontrado: $(python3 --version)"

# Verificar ambiente virtual
if [ ! -d "venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo "Criando ambiente virtual..."
    python3 -m venv venv
    source venv/bin/activate
    echo "Instalando dependências..."
    pip install streamlit requests beautifulsoup4 pandas --no-deps
    pip install altair blinker cachetools click numpy packaging pillow protobuf tenacity toml typing-extensions gitpython pydeck tornado charset-normalizer idna urllib3 certifi python-dateutil pytz tzdata jinja2 jsonschema attrs jsonschema-specifications referencing rpds-py six soupsieve markupsafe narwhals
    pip install "altair>=4.0,<6,!=5.4.0,!=5.4.1"
else
    source venv/bin/activate
fi

# Verificar Streamlit
if ! python -c "import streamlit" 2>/dev/null; then
    echo "❌ Streamlit não está instalado!"
    exit 1
fi
echo "✅ Streamlit está instalado"

# Verificar se a porta está em uso
if lsof -Pi :8501 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "⚠️  Porta 8501 já está em uso!"
    echo "Tentando usar porta 8502..."
    PORT=8502
else
    PORT=8501
fi

echo ""
echo "🚀 Iniciando aplicativo Streamlit..."
echo "📱 Acesse: http://localhost:$PORT"
echo "📝 Pressione Ctrl+C para parar"
echo ""

# Executar Streamlit
streamlit run app.py --server.port $PORT --server.address localhost --server.headless true

