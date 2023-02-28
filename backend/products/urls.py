from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.product_mixin_view),
    path('', views.product_mixin_view),
    path('<int:pk>/delete/', views.product_delete_view),
    path('<int:pk>/update/', views.product_mixin_view ),
    
]