from django.db import models
from django.conf import settings
from decimal import Decimal
from django.utils import timezone

class BankAccount(models.Model):
    ACCOUNT_TYPES = [
        ('current', 'Courant'),
        ('savings', 'Épargne'),
        ('joint', 'Joint'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES, default='current')
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.account_number} - {self.user.username}"

    def generate_account_number(self):
        import random
        return f"{self.user.id:04d}{random.randint(100000, 999999)}"

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = self.generate_account_number()
        super().save(*args, **kwargs)

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('deposit', 'Dépôt'),
        ('withdrawal', 'Retrait'),
        ('transfer', 'Virement'),
    ]

    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    balance_before = models.DecimalField(max_digits=15, decimal_places=2)
    balance_after = models.DecimalField(max_digits=15, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=255, blank=True)
    reference = models.CharField(max_length=50, unique=True, blank=True)
    atm = models.ForeignKey('atm.ATM', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.account.account_number}"

    def save(self, *args, **kwargs):
        if not self.reference:
            import uuid
            self.reference = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)
