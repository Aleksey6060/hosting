from django.shortcuts import redirect
from django.urls import reverse

class RestrictAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_paths = ['/cart/', '/all-products/', '/flowers/', '/order/']
        if any(request.path.startswith(path) for path in restricted_paths):
            if not request.user.is_authenticated:
                return redirect(f"{reverse('login')}?next={request.path}")
        return self.get_response(request)