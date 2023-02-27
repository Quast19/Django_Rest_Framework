import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"
#endpoint = "https://codeforces.com"

re_response = requests.post(endpoint, json = {"title":"Parampuri" ,"content":"Banana fried literally!","price":22}) # Application programming interface 
#re_response = requests.get(endpoint, json = {"Testcase":"Hello world"}) can add a json here, will reflect in the data not in the form part.
# print(re_response.text)
# print(re_response.headers)
# Phone -> Camera , and every app uses camera through an api not directly , securely accessing resources is done using API

#web based api is rest api , there are many web based api , but rest is one of them


#so for using a resource on web we use a web api or here a Rest api

#http request - > gives html 
#rest api request give a JSON , and lets your application work with another application, so Json is done.

#Json java script object notation or JSON, almost like python dictionary or cpp map, 


print(re_response.json()) 


#we can also send it in form of form data so, here
# data = {"RR" : " hai bhai kaise ho "}
# print(re_response.text)

#print(re_response.status_code) -- actual code
# we use all the time, 200 is ok or succeded status code, 300 is we for redirection, 400 for bad request,404 for resourse not found and 500 for internal server errors, there might be more but i will learn em eventually