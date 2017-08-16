import requests
import json

r = requests.get('https://api.github.com/events')

#print(r.content)
print(r.headers)
