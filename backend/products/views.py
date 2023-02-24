from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIview(generics.RetrieveAPIView):
    queryset = Product.objects.all().order_by("?").first()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    
    #product.objects.get(pk = 'abc')
    
product_detail_view = ProductDetailAPIview.as_view()