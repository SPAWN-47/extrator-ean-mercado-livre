# 🔧 Solução de Problemas - Localhost não funciona

## Problemas Comuns e Soluções

### 1. Porta já está em uso

**Sintoma:** Erro ao tentar iniciar o Streamlit

**Solução:**
```bash
# Verificar qual processo está usando a porta 8501
lsof -i :8501

# Matar o processo (substitua PID pelo número do processo)
kill -9 PID

# Ou usar uma porta diferente
streamlit run app.py --server.port 8502
```

### 2. Streamlit não inicia

**Sintoma:** Nada acontece ao executar `./run.sh`

**Solução:**
```bash
# Testar se o Streamlit está instalado
source venv/bin/activate
python -c "import streamlit; print(streamlit.__version__)"

# Se não estiver, reinstalar
pip install streamlit
```

### 3. Erro de importação

**Sintoma:** Erros ao importar módulos

**Solução:**
```bash
source venv/bin/activate
python test_app.py  # Verifica todas as dependências
```

### 4. Browser não abre automaticamente

**Sintoma:** Streamlit inicia mas o navegador não abre

**Solução:**
- Acesse manualmente: `http://localhost:8501`
- Ou use: `http://127.0.0.1:8501`

### 5. Erro relacionado ao pyarrow

**Sintoma:** Avisos sobre pyarrow faltando

**Solução:**
O aplicativo funciona sem pyarrow. Se quiser instalar:
```bash
brew install cmake
pip install pyarrow
```

## Scripts Disponíveis

### `./run.sh` - Início rápido
```bash
./run.sh
```

### `./start.sh` - Início com diagnóstico
```bash
./start.sh
```
Este script verifica o ambiente antes de iniciar e mostra mais informações.

### Teste de dependências
```bash
source venv/bin/activate
python test_app.py
```

## Verificação Manual

1. **Verificar se o ambiente virtual está ativo:**
```bash
which python
# Deve mostrar: .../Mercado Livre/venv/bin/python
```

2. **Verificar se o Streamlit está acessível:**
```bash
source venv/bin/activate
streamlit --version
```

3. **Testar execução direta:**
```bash
source venv/bin/activate
python -m streamlit run app.py
```

## Acesso Manual

Se o navegador não abrir automaticamente, acesse:

- **URL padrão:** http://localhost:8501
- **IP local:** http://127.0.0.1:8501
- **Porta alternativa:** http://localhost:8502 (se 8501 estiver ocupada)

## Logs e Debug

Para ver logs detalhados:
```bash
source venv/bin/activate
streamlit run app.py --logger.level=debug
```

## Reinstalação Completa

Se nada funcionar, reinstale tudo:

```bash
# Remover ambiente virtual
rm -rf venv

# Criar novo ambiente
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install streamlit requests beautifulsoup4 pandas --no-deps
pip install altair blinker cachetools click numpy packaging pillow protobuf tenacity toml typing-extensions gitpython pydeck tornado charset-normalizer idna urllib3 certifi python-dateutil pytz tzdata jinja2 jsonschema attrs jsonschema-specifications referencing rpds-py six soupsieve markupsafe narwhals
pip install "altair>=4.0,<6,!=5.4.0,!=5.4.1"

# Testar
python test_app.py
streamlit run app.py
```

