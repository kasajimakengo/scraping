import requests
from cachecontrol import CacheControl
from cachecontrol.caches import FileCache

session = requests.Session()

cached_session = CacheControl(session, cache=FileCache('.webcache'))

response = cached_session.get('http://docs.python.org/3/')

print(f'from_cache: {response.from_cache}')
print(f'status_code: {response.status_code}')
print(response.text)
