import requests

product_id = input("What is  the product id you want to use?\n")
try:
    product_id = int(product_id)
except:
    print(f'{product_id} not a valid product id')
if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id }/delete"

    res = requests.delete(endpoint) # Application programming interface 
    #print(res.headers)
    if(res.status_code==204):
        print(f"succesfully deleted the product id with {product_id}")
    else:
        print("Invalid request :(")


#
