from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    product_title = request.GET.get("item_name")
    session_title = request.session.get("pr_session_title")
    
    products = Product.objects.all()

    if product_title == "" or product_title is None:
        if session_title:
            del request.session["pr_session_title"]
    elif product_title != "" and product_title is not None:
        request.session["pr_session_title"] = product_title
        products = products.filter(title__icontains=product_title)
    elif session_title:
        products = products.filter(title__icontains=session_title)
    

    paginator = Paginator(products, 4)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    
    return render(request, "shop/index.html", {"products": products})


def detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, "shop/detail.html", {"product": product})