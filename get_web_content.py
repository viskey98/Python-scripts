import urllib.request
import requests

url = 'https://github.com'

response = urllib.request.urlopen(url)
webContent = response.read()
f = open('index.html','wb')
f.write(webContent)
f.close
