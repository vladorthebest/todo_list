from django.core.exceptions import PermissionDenied
from datetime import datetime, timedelta


class UserRequest:
    def __init__(self, ip):
        self.ip = ip
        self.n_requests = 1
        self.time = datetime.now()
    
    def new_requests(self):
        self.n_requests += 1

    def get_requests(self):
        return self.n_requests

    def get_time(self):
        return self.time
    
    def set_time(self):
        self.n_requests = 1
        self.time = datetime.now()



class ErrorTimeIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.users = {}
    
    def __call__(self, request):

        ip = request.META.get('REMOTE_ADDR')
        n = 5   # n requests
        time_n = 10

        if ip not in self.users:
            self.users[ip] = UserRequest(ip)

        else:
            user_requests = self.users[ip]
            user_requests.new_requests()
            time_session = user_requests.get_time()

            if  datetime.now() - time_session > timedelta(seconds=time_n):
                user_requests.set_time()

            elif user_requests.get_requests() >= n:
                raise PermissionDenied
            
        
        response = self.get_response(request)
        return response