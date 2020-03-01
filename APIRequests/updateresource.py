import requests
import json
import jsonpath

url="https://reqres.in/api/users/2"

f=open("C://Users/amruth/Desktop/Hemraj/createnewresource.json",'r')
data=f.read()

json_input=json.loads(data)  #convert data to json format

response=requests.put(url,json_input)
#print(response.status_code)
#print(response.content)   #This will be in string format

#convert the response to json format
json_response=json.loads(response.content)
print(json_response)

job=jsonpath.jsonpath(json_response,'job')
print(job[0])
