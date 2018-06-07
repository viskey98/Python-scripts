from urllib.request import urlopen
import json

if __name__ == "__main__":
	ip = str(input('Enter IP address: '))
	url = "http://www.freegeoip.net/json/{0}".format(ip)
	location_info = json.loads(urlopen(url).read())
	print(location_info)
