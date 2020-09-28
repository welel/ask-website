import functools
import traceback
import logging

from django.db import transaction
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from ask import settings


logger = logging.getLogger('ask')


JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


def ret(json_object, status=200):
    '''Reterns a response with json object.'''
    return JsonResponse(
        json_object,
        status=status,
        safe=not isinstance(json_object, list),
        json_dumps_params=JSON_DUMPS_PARAMS
    )


def error_response(exception):
    '''Form HTTP response with error description and Traceback.'''
    return {'errorMessage': str(exception),
            'traceback': traceback.format_exc()}


def handle_view(fn):
    '''Decorator for views for exception handling.'''
    @functools.wraps(fn)
    def wrapper(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            logger.error(str(error_response(e)))
            if settings.DEBUG:
                return ret(error_response(e), status=500)
            else:
                return HttpResponseRedirect('/')
    return wrapper