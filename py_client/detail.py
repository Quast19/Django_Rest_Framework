import requests

endpoint = "http://localhost:8000/api/products/1/"

res = requests.get(endpoint) # Application programming interface 
#print(res.headers)
print(res.text) 


#
