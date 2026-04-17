from django import forms

class ATMRestockForm(forms.Form):
    amount_added = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01, label="Montant ajouté")