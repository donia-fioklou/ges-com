from django.db import models
from .product import Product
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateField()

    class Meta:
        verbose_name = "Vente"
        verbose_name_plural = "Ventes"

    def __str__(self):
        return f"{self.product.name} - {self.sale_date}"