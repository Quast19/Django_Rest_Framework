import requests

endpoint = "http://localhost:8000/api/products/99999999999/"

res = requests.get(endpoint) # Application programming interface 
#print(res.headers)
print(res.json()) 


#