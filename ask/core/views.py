import functools
import traceback

from django.db import transaction
from django.http import JsonResponse


JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


def error_response(exception):
    '''
    It responses with formed HTTP response with error description
    and Traceback.
    '''
    response = {'errorMessage': str(exception),
                'traceback': traceback.format_exc()}
    return JsonResponse(
        response,
        status=500,
        safe=not isinstance(response, list),
        json_dumps_params=JSON_DUMPS_PARAMS
    )

def handle_view(fn):
    '''Decorator for views for exception handling.'''
    @functools.wraps(fn)
    def wrapper(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return error_response(e)
    return wrapper