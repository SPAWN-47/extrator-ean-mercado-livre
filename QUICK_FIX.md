# ⚡ Solução Rápida - Localhost não funciona

## 🚀 Solução Imediata

### Tente estas opções na ordem:

**1. Use o script Python (mais confiável):**
```bash
cd "/Users/guilhermefonseca/Mercado Livre"
source venv/bin/activate
python3 start_app.py
```

**2. Ou execute diretamente:**
```bash
cd "/Users/guilhermefonseca/Mercado Livre"
source venv/bin/activate
python3 -m streamlit run app.py --server.port 8501
```

**3. Se a porta 8501 estiver ocupada, use outra porta:**
```bash
source venv/bin/activate
python3 -m streamlit run app.py --server.port 8502
```
Depois acesse: http://localhost:8502

## 🔍 Verificar o Problema

**Execute o teste:**
```bash
cd "/Users/guilhermefonseca/Mercado Livre"
source venv/bin/activate
python3 test_app.py
```

Se todos os testes passarem (✅), o problema é apenas de inicialização.

## 📱 Acesso Manual

Se o navegador não abrir automaticamente:

1. **Aguarde a mensagem:** "You can now view your Streamlit app in your browser."
2. **Abra manualmente:** http://localhost:8501
3. **Ou tente:** http://127.0.0.1:8501

## ⚠️ Primeira Execução do Streamlit

Na primeira vez, o Streamlit pode pedir seu email. Você pode:
- **Pressionar Enter** para pular
- **Ou fornecer um email** (opcional)

## 🛑 Se Nada Funcionar

**Reinicie tudo:**
```bash
# Parar qualquer processo do Streamlit
pkill -f streamlit

# Aguardar 2 segundos
sleep 2

# Tentar novamente
cd "/Users/guilhermefonseca/Mercado Livre"
source venv/bin/activate
python3 start_app.py
```

## 📞 Informações para Debug

Se ainda não funcionar, execute e me envie o resultado:

```bash
cd "/Users/guilhermefonseca/Mercado Livre"
source venv/bin/activate
python3 test_app.py
python3 -m streamlit --version
lsof -i :8501
```

