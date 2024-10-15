from django.contrib import admin

from .models import Shop, Product


class ShopAdmin(admin.ModelAdmin):
    """Settings for displaying the Shop model in the admin panel."""
    list_display = ('id', 'name', 'rating')
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    """Settings for displaying the Product model in the admin panel."""
    list_display = (
        'id', 'article_number', 'name', 'color',
        'price_before_discounts', 'price_after_discounts',
        'remainder', 'number_of_reviews', 'rating', 'shop'
    )
    search_fields = ('name', 'article_number', 'color', 'shop__name')
    list_filter = ('shop',)


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
