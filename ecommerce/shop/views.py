from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    products = Product.objects.all()
    product_title = request.GET.get("item_name")

    if product_title != "" and product_title is not None:
        products = products.filter(title__icontains=product_title)

    paginator = Paginator(products, 4)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    
    return render(request, "shop/index.html", {"products": products})
