import requests

endpoint = "http://localhost:8000/api/products/1/update/"
data = {
    "title" : "hello world is updated bruh ",
    "price" : 0,   
}
res = requests.put(endpoint,json = data) # Application programming interface 
#print(res.headers)
print(res.json()) 


#
