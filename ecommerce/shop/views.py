from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Product, Order

# Create your views here.
def index(request):
    product_title = request.GET.get("item-name")
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
    

    paginator = Paginator(products, 8)
    page = request.GET.get("page")
    products = paginator.get_page(page)
    
    return render(request, "shop/index.html", {"products": products})


def detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, "shop/detail.html", {"product": product})


def checkout(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip_code = request.POST.get("zipcode")
        cart_items = request.POST.get("cart-items")
        cart_total = request.POST.get("cart-total")

        new_order = Order(name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, cart_items=cart_items, amount_total=cart_total)
        new_order.save()

        return redirect("index")

    return render(request, "shop/checkout.html")
