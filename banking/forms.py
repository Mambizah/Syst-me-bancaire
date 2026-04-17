from django import forms
from .models import Transaction

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01, label="Montant")

class WithdrawalForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01, label="Montant")

class TransferForm(forms.Form):
    recipient_account = forms.CharField(max_length=20, label="Numéro de compte destinataire")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01, label="Montant")
    description = forms.CharField(max_length=255, required=False, label="Description")