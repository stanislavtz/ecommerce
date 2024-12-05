from django.contrib import admin
from .models import Product, Order

admin.site.site_header = "E-Commerce Administration"
admin.site.site_title = "E-Commerce"
admin.site.index_title = "Manage E-Store"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "discount_price", "category",)
    list_editable = ("price", "discount_price", "category",)
    list_filter = ("title", "category",)
    search_fields = ("title", "category", "price")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "address", "amount_total",)
    list_filter = ("name", "city", "amount_total",)
    search_fields = ("name", "city", "address",)

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
