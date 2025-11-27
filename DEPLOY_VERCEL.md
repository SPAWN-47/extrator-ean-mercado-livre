# 🚀 Deploy no Vercel

**⚠️ IMPORTANTE:** O Streamlit não funciona nativamente no Vercel. Esta é uma versão adaptada usando HTML/JavaScript + Serverless Functions.

## 📋 Pré-requisitos

1. Conta no Vercel (grátis)
2. Node.js instalado (para Vercel CLI)
3. Repositório Git

## 🎯 Opção 1: Deploy via Vercel CLI (Recomendado)

### 1. Instalar Vercel CLI

```bash
npm install -g vercel
```

### 2. Fazer Login

```bash
vercel login
```

### 3. Deploy

```bash
# No diretório do projeto
vercel

# Para produção
vercel --prod
```

## 🎯 Opção 2: Deploy via GitHub

### 1. Criar Repositório no GitHub

```bash
git init
git add .
git commit -m "Deploy Vercel: Extrator EAN"
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git push -u origin main
```

### 2. Conectar no Vercel

1. Acesse: https://vercel.com
2. Faça login com GitHub
3. Clique em "Add New Project"
4. Importe seu repositório
5. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: ./
   - **Build Command**: (deixe vazio)
   - **Output Directory**: public

### 3. Deploy Automático

O Vercel fará deploy automático a cada push!

## 📁 Estrutura de Arquivos

```
.
├── api/
│   └── extract.py          # Serverless function
├── public/
│   └── index.html          # Interface web
├── vercel.json             # Configuração Vercel
└── requirements.txt        # Dependências Python
```

## 🔧 Configuração

O arquivo `vercel.json` já está configurado com:
- ✅ Serverless function em Python
- ✅ Rota `/api/extract`
- ✅ Timeout de 30 segundos
- ✅ CORS habilitado

## 🌐 URL Final

Após o deploy, você terá uma URL como:
```
https://seu-projeto.vercel.app
```

## ⚠️ Limitações

- ⏱️ Timeout máximo: 30 segundos (plano gratuito)
- 📦 Tamanho máximo: 50MB
- 🔄 Cold start pode demorar ~2-3 segundos na primeira requisição

## 🔄 Atualizações

Após fazer push no GitHub, o Vercel atualiza automaticamente!

## 💰 Custo

**GRATUITO** para uso pessoal!

## 🆚 Comparação: Streamlit Cloud vs Vercel

| Recurso | Streamlit Cloud | Vercel |
|---------|----------------|--------|
| Facilidade | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Performance | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Timeout | Sem limite | 30s (gratuito) |
| Interface | Streamlit nativo | HTML/JS customizado |
| **Recomendado para:** | ✅ Streamlit apps | ✅ Web apps genéricos |

**💡 Recomendação:** Use **Streamlit Cloud** se quiser manter o app Streamlit original!

