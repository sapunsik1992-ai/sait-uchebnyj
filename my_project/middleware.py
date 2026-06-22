"""
Middleware для отключения Content Security Policy (CSP).
Нужен для работы AI-помощника, который делает запросы к HuggingFace API.
"""

from django.utils.deprecation import MiddlewareMixin


class DisableCSPMiddleware(MiddlewareMixin):
    """Отключает CSP-заголовки для работы AI-помощника."""
    
    def process_response(self, request, response):
        # Удаляет CSP-заголовок, если он установлен
        if 'Content-Security-Policy' in response:
            del response['Content-Security-Policy']
        if 'X-Content-Security-Policy' in response:
            del response['X-Content-Security-Policy']
        if 'X-WebKit-CSP' in response:
            del response['X-WebKit-CSP']
        return response
