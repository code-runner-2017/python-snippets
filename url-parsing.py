from urllib.parse import urlparse
from urllib.parse import urlencode
from urllib.parse import parse_qs, parse_qsl
from urllib.parse import quote, quote_plus, urlencode

# More here: https://pymotw.com/3/urllib.parse/index.html

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print(parsed) # ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')

# access to all parts: 
print('query   :', parsed.query)  # prints: query=arg

# Unparsing

original = 'http://netloc/path;param?query=arg#frag'
print('ORIG  :', original)
parsed = urlparse(original)
print('PARSED:', parsed.geturl())

# Encoding query arguments

query_args = {
    'q': 'query string',
    'foo': 'bar',
}
encoded_args = urlencode(query_args) 
print('Encoded:', encoded_args)  # q=query+string&foo=bar

query_args = {
    'foo': ['foo1', 'foo2'],
}
print('Single  :', urlencode(query_args))  # foo=%5B%27foo1%27%2C+%27foo2%27%5D 
print('Sequence:', urlencode(query_args, doseq=True)) # foo=foo1&foo=foo2

encoded = 'foo=foo1&foo=foo2'

print('parse_qs :', parse_qs(encoded)) # parse_qs : {'foo': ['foo1', 'foo2']}
print('parse_qsl:', parse_qsl(encoded)) # parse_qsl: [('foo', 'foo1'), ('foo', 'foo2')]

url = 'http://localhost:8080/~hellmann/'
print('urlencode() :', urlencode({'url': url}))  # urlencode() : url=http%3A%2F%2Flocalhost%3A8080%2F~hellmann%2F
print('quote()     :', quote(url))  # quote(): http%3A//localhost%3A8080/~hellmann/
print('quote_plus():', quote_plus(url)) # quote_plus(): http%3A%2F%2Flocalhost%3A8080%2F~hellmann%2F
