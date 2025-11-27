# 🚀 Guia de Deploy Completo

Você tem **2 opções** para fazer deploy do aplicativo:

## 🎯 Opção 1: Streamlit Cloud (RECOMENDADO) ⭐

**✅ Melhor para:** Manter o app Streamlit original  
**✅ Mais fácil:** Deploy em 2 minutos  
**✅ Gratuito:** Sem limites de uso  

👉 **Siga o guia:** `DEPLOY_STREAMLIT_CLOUD.md`

### Resumo Rápido:
1. Faça push do código para GitHub
2. Acesse https://share.streamlit.io/
3. Conecte seu repositório
4. Deploy automático! 🎉

---

## 🎯 Opção 2: Vercel

**✅ Melhor para:** Interface web customizada  
**⚠️ Requer:** Adaptação do código (já feita!)  
**✅ Gratuito:** Com algumas limitações  

👉 **Siga o guia:** `DEPLOY_VERCEL.md`

### Resumo Rápido:
1. Instale Vercel CLI: `npm install -g vercel`
2. Execute: `vercel` no diretório do projeto
3. Ou conecte via GitHub no dashboard do Vercel

---

## 📊 Comparação

| Recurso | Streamlit Cloud | Vercel |
|---------|----------------|--------|
| **Facilidade** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Performance** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Timeout** | Sem limite | 30s (gratuito) |
| **Interface** | Streamlit nativo | HTML/JS customizado |
| **Setup** | 2 minutos | 5 minutos |
| **Manutenção** | Automático | Automático |

## 💡 Recomendação

**Use Streamlit Cloud** se você quer:
- ✅ Manter o app Streamlit original
- ✅ Deploy mais rápido
- ✅ Sem preocupação com timeout

**Use Vercel** se você quer:
- ✅ Interface totalmente customizada
- ✅ Melhor performance
- ✅ Integração com outras ferramentas

---

## 🚀 Quick Start

### Streamlit Cloud (2 minutos)
```bash
git init
git add .
git commit -m "Deploy Streamlit Cloud"
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git push -u origin main
# Depois: https://share.streamlit.io/
```

### Vercel (5 minutos)
```bash
npm install -g vercel
vercel login
vercel
```

---

## 📁 Arquivos de Deploy

- `DEPLOY_STREAMLIT_CLOUD.md` - Guia completo Streamlit Cloud
- `DEPLOY_VERCEL.md` - Guia completo Vercel
- `vercel.json` - Configuração Vercel
- `api/extract.py` - Serverless function (Vercel)
- `public/index.html` - Interface web (Vercel)
- `.streamlit/config.toml` - Config Streamlit Cloud

---

## ❓ Dúvidas?

Consulte os guias específicos:
- 📖 `DEPLOY_STREAMLIT_CLOUD.md`
- 📖 `DEPLOY_VERCEL.md`

