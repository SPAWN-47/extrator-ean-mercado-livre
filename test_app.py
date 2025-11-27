#!/usr/bin/env python3
"""
Script de teste para verificar se todas as dependências estão funcionando
"""

import sys

def test_imports():
    """Testa todas as importações necessárias"""
    errors = []
    
    try:
        import streamlit as st
        print(f"✅ Streamlit {st.__version__} - OK")
    except ImportError as e:
        errors.append(f"❌ Streamlit: {e}")
    
    try:
        import requests
        print(f"✅ Requests {requests.__version__} - OK")
    except ImportError as e:
        errors.append(f"❌ Requests: {e}")
    
    try:
        from bs4 import BeautifulSoup
        print("✅ BeautifulSoup4 - OK")
    except ImportError as e:
        errors.append(f"❌ BeautifulSoup4: {e}")
    
    try:
        import pandas as pd
        print(f"✅ Pandas {pd.__version__} - OK")
    except ImportError as e:
        errors.append(f"❌ Pandas: {e}")
    
    try:
        import json
        import time
        import random
        from io import StringIO
        from typing import Optional, Dict, List
        import re
        print("✅ Bibliotecas padrão - OK")
    except ImportError as e:
        errors.append(f"❌ Bibliotecas padrão: {e}")
    
    # Tentar importar o app
    try:
        import app
        print("✅ app.py - Importado com sucesso")
    except Exception as e:
        errors.append(f"❌ app.py: {e}")
    
    if errors:
        print("\n❌ Erros encontrados:")
        for error in errors:
            print(f"  {error}")
        return False
    else:
        print("\n✅ Todas as dependências estão funcionando!")
        return True

if __name__ == "__main__":
    print("🔍 Verificando dependências...\n")
    success = test_imports()
    sys.exit(0 if success else 1)

