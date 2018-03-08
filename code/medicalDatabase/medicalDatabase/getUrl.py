import requests

class getUrl():
	result = requests.get('http://127.0.0.1:9984/api/v1/transactions/d9971cb8074e6d3e7a71b95dbdace0466a6d8f9759e583d1911c619f55a62e18')
	print(result.text)
