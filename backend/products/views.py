from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
    
product_list_create_view =ProductListCreateAPIView.as_view()


class ProductDetailAPIview(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_detail_view = ProductDetailAPIview.as_view()

class ProductListAPIview(generics.ListAPIView):
    '''
    Not Gonna use this method
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_list_view = ProductListAPIview.as_view()

@api_view(["GET", "POST"])
def product_alt_view(request,pk= None ,*args, **kwargs):
    method = request.method
    
    
    if method == "GET":
        #can be detail or list view now, so we need to differ with help of primary key.
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product, pk = pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)
    if method== "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):#for robust message use raise_exception
            #print(serializer.validated_data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content = content)
            return Response(serializer.data)
        return Response({"invalid":"not good data, or in serializable data"}, status = 400)