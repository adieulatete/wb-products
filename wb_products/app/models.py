from django.db import models


class Shop(models.Model):
    """Model representing the shop."""
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    """Model representing the product."""
    article_number = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=40)
    price_before_discounts = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_after_discounts = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remainder = models.IntegerField(default=0)
    number_of_reviews = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    shop = models.ForeignKey(Shop, related_name='shop', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
