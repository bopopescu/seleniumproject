import requests
import json
import jsonpath

url="https://reqres.in/api/users"

f=open("C://Users/amruth/Desktop/Hemraj/createnewresource.json",'r')
data=f.read()

#convert data to json format
json_input=json.loads(data)
print(json_input)

#post data to server
response=requests.post(url,json_input)
print(response.content)
#print(response.headers.get('Content-Length'))

#convert response to json
json_response=json.loads(response.content)
print(json_response)

#fetch any one value fom whole content
id=jsonpath.jsonpath(json_response,'id')
print(id[0])

