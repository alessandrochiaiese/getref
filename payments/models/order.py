
from django.db import models
from .product import Product
from django.contrib.auth.models import User  # Presupponiamo che tu stia usando il modello User di default per il cliente
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]
    # Relazione tra un ordine e un cliente
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Customer"))  # Associa l'ordine a un cliente
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))  # Data e ora di creazione dell'ordine
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending', verbose_name=_("Status"))  # Stato dell'ordine
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Price"))  # Prezzo totale dell'ordine
    products = models.ManyToManyField(Product, through='OrderItem', verbose_name=_("Products"))  # Relazione molti-a-molti con prodotto tramite il modello intermedio

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username} - {self.status}"

    # Calcolo automatico del prezzo totale in base ai prodotti ordinati
    def calculate_total_price(self):
        total = sum(item.total_price() for item in self.order_items.all())
        self.total_price = total
        self.save()

    class Meta:
        ordering = ("-created_at",)
        db_table = 'my_orders'
        verbose_name = 'MyCustomOrder'
        verbose_name_plural = 'MyCustomOrders'

class OrderItem(models.Model):
    # Modello intermedio per la relazione tra Order e Product
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # Quantità di prodotto ordinata

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


    class Meta:
        ordering = ("-created_at",)
        db_table = 'my_custom_order_items'
        verbose_name = 'MyCustomOrderItem'
        verbose_name_plural = 'MyCustomOrderItems'