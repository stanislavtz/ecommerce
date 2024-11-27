from django.shortcuts import render
from .models import Product
from django.shortcuts import get_list_or_404


# Create your views here.
def index(request):
    products = Product.objects.all()
    
    return render(request, "shop/index.html", {"products": products})
