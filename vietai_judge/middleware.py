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

    def process_request(self, request):
        client_ip = request.META['REMOTE_ADDR']
        msg = '[Audit] IP: %s' % (client_ip)
        print(msg)
