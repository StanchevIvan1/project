from django.contrib import admin

from watch_shop.web.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
