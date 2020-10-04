import logging

from django.core.paginator import Paginator, EmptyPage


logger = logging.getLogger('ask')


def paginate(request, query_set):
    '''Pages limit validation, returns Paginator and current page.'''
    try:
        limit = int(request.GET.get('limit', 15))
    except ValueError:
        logger.warning('''Client trying to send incorrect query param `limit`.
        Expected int value, but {} was send. Value: {}'''.format(
            type(request.GET.get('limit')),
            request.GET.get('limit')
        ))
        limit = 15
    if limit > 100:
        limit = 100
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(query_set, limit)
    try:
        page = paginator.page(page)
    except EmptyPage: 
        page = paginator.page(paginator.num_pages)
    return paginator, page
