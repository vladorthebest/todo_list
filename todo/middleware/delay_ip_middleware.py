from time import sleep
from django.core.exceptions import PermissionDenied

class DealyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.n = 1 
    
    def __call__(self, request):

        n = 5 # n * request

        if self.n == n:
            sleep(5)
            self.n = 1 
        else:
            self.n+=1
        
        response = self.get_response(request)
        return response