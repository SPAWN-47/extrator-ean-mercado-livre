"""
Redirect root to index.html - Fallback handler
"""
from http.server import BaseHTTPRequestHandler

def handler(request):
    # This is a fallback - Vercel should serve index.html automatically
    return (200, {'Content-Type': 'text/html'}, '<html><body><h1>Redirecting...</h1><script>window.location.href="/index.html";</script></body></html>')

