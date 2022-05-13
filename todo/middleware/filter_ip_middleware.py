from django.core.exceptions import PermissionDenied
from time import sleep

class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        
        response = self.get_response(request)

        return response