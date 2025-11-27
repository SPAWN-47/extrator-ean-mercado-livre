#!/usr/bin/env python3
"""
Script Python para iniciar o aplicativo Streamlit
Use este script se os scripts shell não funcionarem
"""

import sys
import os
import subprocess

def main():
    # Mudar para o diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print("🔍 Verificando ambiente...")
    print(f"📁 Diretório: {script_dir}")
    print()
    
    # Verificar se o app.py existe
    if not os.path.exists("app.py"):
        print("❌ Erro: app.py não encontrado!")
        sys.exit(1)
    
    # Verificar dependências
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} encontrado")
    except ImportError:
        print("❌ Erro: Streamlit não está instalado!")
        print("Execute: pip install streamlit")
        sys.exit(1)
    
    try:
        import requests
        import bs4
        import pandas
        print("✅ Todas as dependências estão instaladas")
    except ImportError as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)
    
    print()
    print("🚀 Iniciando aplicativo Streamlit...")
    print("📱 O aplicativo abrirá em: http://localhost:8501")
    print("📝 Pressione Ctrl+C para parar")
    print()
    
    # Executar Streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n\n👋 Aplicativo encerrado pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao executar Streamlit: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

