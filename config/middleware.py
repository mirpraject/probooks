from django.conf import settings
from django.http import HttpResponse

class HTMXLoginMiddleware:
    """
    Middleware to intercept 302 redirects to the login page originating from HTMX requests.
    Instead of letting HTMX inject the login page's HTML into the current DOM,
    it instructs HTMX to perform a full page redirect.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if this is an HTMX request that resulted in a redirect
        if request.headers.get('HX-Request') == 'true' and response.status_code == 302:
            # If the redirect is to the login page (session expired/unauthenticated)
            if response.url.startswith(settings.LOGIN_URL):
                # Create an empty response with HX-Redirect header
                # This makes HTMX redirect the entire browser window instead of swapping HTML
                htmx_response = HttpResponse('')
                htmx_response['HX-Redirect'] = response.url
                return htmx_response
                
        return response
