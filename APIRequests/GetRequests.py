import requests
import json
import jsonpath

url="https://reqres.in/api/users?page=2"

response=requests.get(url)
print(response)
#print(response.content) # This is will fetch whole content of page
#print(response.headers)
#assert response.status_code == 200 # to compare response result

# convert response to json format
json_format=json.loads(response.text)
#print(json_format)

#Fetch aany one content from whole page
total=email=jsonpath.jsonpath(json_format,'total')  # this returns list
print(total[0])
