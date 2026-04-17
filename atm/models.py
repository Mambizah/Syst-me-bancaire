from django.db import models
from decimal import Decimal

class ATM(models.Model):
    STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('maintenance', 'En maintenance'),
        ('out_of_service', 'Hors service'),
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='available')
    cash_available = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    max_withdrawal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('500.00'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.city}"

class ATMRestock(models.Model):
    atm = models.ForeignKey(ATM, on_delete=models.CASCADE, related_name='restocks')
    amount_added = models.DecimalField(max_digits=15, decimal_places=2)
    restocked_by = models.CharField(max_length=100)  # Could be user later
    restocked_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Restock {self.atm.name} - {self.amount_added}"
