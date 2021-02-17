from urllib.parse import urlparse

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print(parsed) # ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')