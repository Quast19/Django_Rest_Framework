# from django.shortcuts import render
# from django.http import JsonResponse , HttpResponse useless as drf response is used
import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response #will take over the json response
from rest_framework.decorators import api_view #convert function to an api view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by("?").first()    
    # data= {}
    # if instance:
    #     #data = model_to_dict(instance)
    #     data = ProductSerializer(instance).data  
    #getting data from the models here code
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):#for robust message use raise_exception
        #instance = serializer.save()
        serializer.save()
        print(serializer.data)
    #getting data from the post request
        return Response(serializer.data)
    return Response({"invalid":"not good data, or in serializable data"}, status = 400)#if raise exception is not used, used this
    # return JsonResponse(data) before drf response to return json file
#in order to send the response as httpresponse we need to serialize the data, but Decimal data is non serializable and convert it to json string which is also tedious, this is where django rest  framework will help us :)
    #     json_data_str = json.dumps(data)      
    # return HttpResponse(json_data_str, headers = {'content-type':'application/json'})#so by content type is text/html 


#all the below code can be replaced by converting your data to dictionary easily using model_to _ dict
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
# # The previous functions explaining somethings
#     # request is a instance of httprequest class, provided by django framework, not the same as python request
#     #flow = basic.py ->requested this function, before returning we printed the json data and returned our json data
#     print(request.body)
#     body = request.body
#     data = {}
#     #data['message'] = "Hi there this is your django api response"
#     try:
#         data = json.loads(body) #json data to python dictionary, we put it in try block because if body has no json then we can come across error
#     except:
#         pass
#     print(data.keys())
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     print(request.headers)
#     #return JsonResponse({"message:":" Hi there this is your django api response "})
#     return JsonResponse(data)
# # Create your views here.
