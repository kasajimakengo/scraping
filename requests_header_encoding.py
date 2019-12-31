import sys
import requests

url = sys.argv[1]
r = requests.get(url)

print(f'encoding: {r.encoding}', file=sys.stderr)
print(r.text)