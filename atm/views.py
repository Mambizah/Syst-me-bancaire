from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from .models import ATM, ATMRestock
from .forms import ATMRestockForm

def atm_list(request):
    atms = ATM.objects.all()
    return render(request, 'atm/atm_list.html', {'atms': atms})

@login_required
@user_passes_test(lambda u: u.is_staff)
def atm_restock(request, atm_id):
    atm = get_object_or_404(ATM, id=atm_id)
    if request.method == 'POST':
        form = ATMRestockForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount_added']
            with transaction.atomic():
                atm.cash_available += amount
                atm.save()
                ATMRestock.objects.create(
                    atm=atm,
                    amount_added=amount,
                    restocked_by=request.user.username
                )
            messages.success(request, f'Rechargement de {amount} € effectué.')
            return redirect('atm_list')
    else:
        form = ATMRestockForm()
    return render(request, 'atm/atm_restock.html', {'form': form, 'atm': atm})
