import sys
import re
import requests

url = sys.argv[1]
r = requests.get(url)
scanned_text = r.content[:1024].decode('ascii', errors='replace')
match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
if match:
    r.encoding = match.group(1)
else:
    r.encoding = 'utf-8'

print(f'encoding: {r.encoding}', file=sys.stderr)
print(r.text)