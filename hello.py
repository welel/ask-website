def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    response_body = '\n'.join(environ['QUERY_STRING'].split('&')).encode()

    start_response(status, headers)
    return iter([response_body])

'''
if __name__ == '__main__':
    environ = {'QUERY_STRING':'a=1&a=2&b=3'}

    print(application(environ, ''))
'''
