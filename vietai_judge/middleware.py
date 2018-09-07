import logging
import re


logger = logging.getLogger(__name__)

class LogIPMiddleware(object):
    IGNORED_PATHS = [
        '/backend/register_push_token/',
        '/backend/user_settings/',
        '/calendars/airbnb_ajax_log/',
        '/inbound/sendgrid/'
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def process_request(self, request):
        client_ip = self.get_client_ip(request)
        msg = '[Audit] IP: %s' % (client_ip)
        print(msg)
