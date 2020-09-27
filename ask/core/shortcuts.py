from django.core.paginator import Paginator, EmptyPage


def paginate(request, query_set):
    '''Pages limit validation, returns Paginator and current page.'''
    try:
        limit = int(request.GET.get('limit', 15))
    except ValueError:
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
