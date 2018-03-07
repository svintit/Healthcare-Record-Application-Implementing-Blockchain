import requests

class getUrl():
	result = requests.get('http://www.google.com')
	print(result.text)