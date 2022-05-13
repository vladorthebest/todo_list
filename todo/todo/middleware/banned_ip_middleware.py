from django.core.exceptions import PermissionDenied

class FilterBannedIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        
        banned_ips = []

        ip = request.META.get('REMOTE_ADDR')
        if ip in banned_ips:
            raise PermissionDenied
        
        response = self.get_response(request)

        return response