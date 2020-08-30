from urllib import parse

pythonpath='/home/pavel/web/'
bind = '0.0.0.0:8080'

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    query_params = parse.parse_qs(environ['QUERY_STRING'])
    answer = ''.join([key + '=' + ''.join(value) + '\n' for key, value in query_params.items()]).encode()

    start_response(status, headers)
    return iter([answer])
