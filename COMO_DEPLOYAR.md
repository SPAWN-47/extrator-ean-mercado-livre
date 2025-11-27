# 🚀 Como Fazer Deploy - Guia Rápido

## ⚡ Opção Mais Rápida: Streamlit Cloud (2 minutos)

### Passo 1: Criar Repositório no GitHub

```bash
# No terminal, dentro da pasta do projeto
git init
git add .
git commit -m "Extrator EAN Mercado Livre"
```

Depois, crie um repositório no GitHub e faça:
```bash
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git branch -M main
git push -u origin main
```

### Passo 2: Deploy no Streamlit Cloud

1. Acesse: **https://share.streamlit.io/**
2. Faça login com GitHub
3. Clique em **"New app"**
4. Selecione seu repositório
5. **Main file path:** `app.py`
6. Clique em **"Deploy"**

**Pronto!** 🎉 Seu app estará online em ~1 minuto!

---

## 🌐 Opção Alternativa: Vercel

### Passo 1: Instalar Vercel CLI

```bash
npm install -g vercel
```

### Passo 2: Deploy

```bash
# No diretório do projeto
vercel login
vercel
```

Siga as instruções na tela. Pronto! 🚀

---

## 📝 Qual Escolher?

- **Streamlit Cloud:** ✅ Mais fácil, mantém o app original
- **Vercel:** ✅ Interface customizada, melhor performance

**Recomendação:** Comece com **Streamlit Cloud** (mais rápido)!

---

## 🔗 Links Úteis

- Streamlit Cloud: https://share.streamlit.io/
- Vercel: https://vercel.com
- GitHub: https://github.com

