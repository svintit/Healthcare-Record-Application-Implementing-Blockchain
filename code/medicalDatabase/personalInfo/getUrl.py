import requests
import models

def getUrl(link):
		r = requests.get(link)
		results = r.json()
		print (results)
		#for result in results['record']:
		#	getUrl.object.create(
		#		fullName=request['fullName'],
		#		address=request['address'],
		#		gender=request['gender'],
		#		homePhone=request['homePhone'],
		#		personalPhone=request['personalPhone'],
		#		emergencyContact=request['emergencyContact'],
		#		email=request['email'],
		#		ppsn=request['ppsn'],
		#		maritalStatus=request['maritalStatus'],
		#		employment=request['employment'],
		#		personalPic=request['personalPic'],
			#)
		#context = {'results': UserProfile.objects.all()}

getUrl('http://127.0.0.1:9984/api/v1/transactions/3e03a130666501f4403e2d1d904424321940c6014e012596c2ca534136e18dfb')
