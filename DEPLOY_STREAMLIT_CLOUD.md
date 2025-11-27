# 🚀 Deploy no Streamlit Cloud (RECOMENDADO)

O Streamlit Cloud é a plataforma oficial e gratuita para hospedar aplicativos Streamlit.

## 📋 Pré-requisitos

1. Conta no GitHub
2. Repositório GitHub com seu código
3. Conta no Streamlit Cloud (grátis)

## 🎯 Passo a Passo

### 1. Criar Repositório no GitHub

```bash
# Inicializar git (se ainda não fez)
git init
git add .
git commit -m "Initial commit: Extrator EAN Mercado Livre"

# Criar repositório no GitHub e fazer push
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
git branch -M main
git push -u origin main
```

### 2. Acessar Streamlit Cloud

1. Acesse: https://share.streamlit.io/
2. Faça login com sua conta GitHub
3. Clique em "New app"

### 3. Configurar o Deploy

- **Repository**: Selecione seu repositório
- **Branch**: `main` (ou a branch que você usa)
- **Main file path**: `app.py`
- **App URL**: Escolha um nome único (ex: `extrator-ean-mercado-livre`)

### 4. Deploy Automático

O Streamlit Cloud irá:
- ✅ Instalar automaticamente as dependências do `requirements.txt`
- ✅ Fazer deploy automático a cada push no GitHub
- ✅ Fornecer uma URL pública (ex: `https://extrator-ean-mercado-livre.streamlit.app`)

## 📝 Arquivos Necessários

Certifique-se de ter estes arquivos no repositório:

- ✅ `app.py` - Aplicativo principal
- ✅ `requirements.txt` - Dependências Python
- ✅ `.streamlit/config.toml` - Configurações (opcional)

## 🔄 Atualizações

Após fazer push no GitHub, o Streamlit Cloud atualiza automaticamente em ~1 minuto.

## 💰 Custo

**GRATUITO** para uso pessoal e projetos públicos!

## 🌐 URL Final

Seu app estará disponível em:
```
https://SEU-APP-NAME.streamlit.app
```

