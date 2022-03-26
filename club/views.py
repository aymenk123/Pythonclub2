from django.shortcuts import render,get_object_or_404
from .models import Product, PythonType, Review
from .forms import ProductForm 
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
 return render(request,'club/index.html')

def products(request):
    product_list=Product.objects.all()
    return render(request, 'club/products.html',{'product_list' : product_list})

def ProductDetail(request, id): 
    product=get_object_or_404(product, pk=id)
    return render(request, 'club/productdetail.html', {'product' : product})

@login_required
def newProduct(request):
     form=ProductForm
     
     if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
             post=form.save(commit=True)
             post.save()
             form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'club/newproduct.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')