import sys

from django.conf import settings
from django.views.debug import technical_500_response


class UserBasedExceptionMiddleware:
    """
    This middleware provide superusers with access to de settings.DEBUG = True when 500 error page occur in production
    or DEBUG = False
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called
        response = self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        return response

    def process_exception(self, request, exception):
        if request.user.is_superuser and not settings.DEBUG:
            return technical_500_response(request, *sys.exc_info())
