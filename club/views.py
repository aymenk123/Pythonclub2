from django.shortcuts import render,get_object_or_404
from .models import Product, PythonType, Review

# Create your views here.
def index(request):
 return render(request,'club/index.html')

def products(request):
    product_list=Product.objects.all()
    return render(request, 'club/products.html',{'product_list' : product_list})

def ProductDetail(request, id): 
    product=get_object_or_404(product, pk=id)
    return render(request, 'club/productdetail.html', {'product' : product})