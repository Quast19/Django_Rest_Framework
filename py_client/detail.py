import requests

endpoint = "http://127.0.0.1:8000/api/products/1/"

res = requests.get(endpoint) # Application programming interface 

print(res.text) 


#