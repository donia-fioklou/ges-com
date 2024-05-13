from django.db import models
from .product import Product
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()

    class Meta:
        verbose_name = "Achat"
        verbose_name_plural = "Achats"

    def __str__(self):
        return f"{self.product.name} - {self.purchase_date}"