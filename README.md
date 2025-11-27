# 🛒 Extrator de EAN/GTIN - Mercado Livre

Aplicativo web local desenvolvido com Streamlit para extração em massa de códigos EAN/GTIN de produtos do Mercado Livre.

## 🚀 Instalação

1. **Crie e ative o ambiente virtual:**
```bash
python3 -m venv venv
source venv/bin/activate
```

2. **Instale as dependências:**
```bash
pip install streamlit requests beautifulsoup4 pandas --no-deps
pip install altair blinker cachetools click numpy packaging pillow protobuf tenacity toml typing-extensions gitpython pydeck tornado charset-normalizer idna urllib3 certifi python-dateutil pytz tzdata jinja2 jsonschema attrs jsonschema-specifications referencing rpds-py six soupsieve markupsafe narwhals
pip install "altair>=4.0,<6,!=5.4.0,!=5.4.1"
```

**Nota:** O `pyarrow` não é instalado por padrão pois requer `cmake`. O aplicativo funciona sem ele para funcionalidades básicas. Se precisar de funcionalidades avançadas do Streamlit, instale o `cmake` primeiro:
```bash
brew install cmake
pip install pyarrow
```

## 📖 Como Usar

### Opção 1: Script Shell (Recomendado)
```bash
./run.sh
```

### Opção 2: Script com Diagnóstico
```bash
./start.sh
```

### Opção 3: Script Python
```bash
python3 start_app.py
```

### Opção 4: Manual
```bash
source venv/bin/activate
streamlit run app.py
```

**Nota:** Se o localhost não funcionar, consulte o arquivo `SOLUCAO_PROBLEMAS.md` para soluções.

2. **No navegador que abrir:**
   - Cole uma lista de URLs do Mercado Livre (uma por linha) na área de texto
   - Clique em "Extrair Dados"
   - Aguarde o processamento (com barra de progresso em tempo real)
   - Visualize os resultados na tabela
   - Baixe os resultados em CSV clicando em "Baixar CSV"

## ✨ Funcionalidades

- ✅ Extração de códigos EAN/GTIN de múltiplas URLs
- ✅ Extração de títulos dos produtos
- ✅ Visualização em tempo real dos resultados
- ✅ Barra de progresso durante o processamento
- ✅ Delay aleatório entre requisições (0.5-2s) para evitar bloqueios
- ✅ Exportação dos resultados em CSV
- ✅ Headers personalizados para evitar bloqueios
- ✅ Tratamento de erros robusto
- ✅ Interface intuitiva e responsiva

## 📋 Formato de Entrada

Cole as URLs uma por linha, por exemplo:
```
https://produto.mercadolivre.com.br/MLB-1234567890
https://produto.mercadolivre.com.br/MLB-0987654321
https://www.mercadolivre.com.br/produto/MLB-1122334455
```

## 📊 Formato de Saída

O CSV exportado contém as seguintes colunas:
- **Status**: ✅ (sucesso) ou ❌ (erro)
- **EAN/GTIN**: Código extraído ou "Não encontrado"
- **Título**: Título do produto ou "Não encontrado"
- **URL**: URL original processada

## 🔧 Tecnologias Utilizadas

- **Streamlit**: Framework para aplicações web
- **Requests**: Biblioteca para requisições HTTP
- **BeautifulSoup4**: Parser HTML
- **Pandas**: Manipulação de dados e exportação CSV

## ⚠️ Notas Importantes

- O aplicativo usa delays aleatórios entre requisições para evitar bloqueios
- Headers personalizados são usados para simular um navegador real
- Timeout de 15 segundos por requisição
- O código tenta múltiplas estratégias para encontrar o EAN (JSON-LD e scripts JavaScript)

## 📝 Licença

Este projeto é fornecido como está, para uso pessoal.

