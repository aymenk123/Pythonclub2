from django.urls import path
from . import views 

urlpatterns = [
   path('',views.index, name='index'),
   path('products/', views.products, name='products'),
   path('ProductDetail/<int:id>', views.ProductDetail,  name='detail'),
   path('newProduct/', views.newProduct, name='newproduct'),
   path('loginmessage/', views.loginmessage, name='loginmessage'),
   path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
