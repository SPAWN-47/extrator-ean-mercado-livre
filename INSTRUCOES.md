# 📋 Instruções Rápidas de Uso

## 🚀 Iniciar o Aplicativo

### Opção 1: Usando o script (Recomendado)
```bash
./run.sh
```

### Opção 2: Manualmente
```bash
source venv/bin/activate
streamlit run app.py
```

O aplicativo abrirá automaticamente no navegador em `http://localhost:8501`

## 📝 Como Usar

1. **Cole as URLs**: Na área de texto, cole uma lista de URLs do Mercado Livre (uma por linha)
   ```
   https://produto.mercadolivre.com.br/MLB-1234567890
   https://produto.mercadolivre.com.br/MLB-0987654321
   ```

2. **Clique em "Extrair Dados"**: O sistema processará cada URL automaticamente

3. **Aguarde o processamento**: 
   - Barra de progresso mostra o andamento
   - Tabela atualiza em tempo real
   - Delay aleatório entre requisições (0.5-2s) para evitar bloqueios

4. **Visualize os resultados**: 
   - Status: ✅ (sucesso) ou ❌ (erro)
   - EAN/GTIN: Código extraído
   - Título: Nome do produto
   - URL: Link original

5. **Exporte em CSV**: Clique no botão "📥 Baixar CSV" para salvar os resultados

## ⚙️ Funcionalidades

- ✅ Extração automática de EAN/GTIN de múltiplas URLs
- ✅ Extração de títulos dos produtos
- ✅ Visualização em tempo real
- ✅ Barra de progresso
- ✅ Delay aleatório para evitar bloqueios
- ✅ Exportação em CSV
- ✅ Tratamento robusto de erros

## 🔧 Solução de Problemas

### Erro: "command not found: pip"
Use `python3 -m pip` ou `pip3` em vez de `pip`

### Erro relacionado ao pyarrow
O aplicativo funciona sem pyarrow. Se precisar dele:
```bash
brew install cmake
pip install pyarrow
```

### O aplicativo não abre no navegador
Acesse manualmente: `http://localhost:8501`

## 📊 Formato do CSV Exportado

O arquivo CSV contém as seguintes colunas:
- **Status**: ✅ ou ❌
- **EAN/GTIN**: Código extraído ou "Não encontrado"
- **Título**: Nome do produto ou "Não encontrado"
- **URL**: URL original processada

