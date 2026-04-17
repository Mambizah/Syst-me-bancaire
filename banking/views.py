from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from decimal import Decimal
from .models import BankAccount, Transaction
from .forms import DepositForm, WithdrawalForm, TransferForm

@login_required
def account_detail(request, account_id):
    account = get_object_or_404(BankAccount, id=account_id, user=request.user)
    transactions = account.transactions.order_by('-timestamp')[:10]
    return render(request, 'banking/account_detail.html', {
        'account': account,
        'transactions': transactions
    })

@login_required
def deposit(request, account_id):
    account = get_object_or_404(BankAccount, id=account_id, user=request.user)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            with transaction.atomic():
                balance_before = account.balance
                account.balance += amount
                account.save()
                Transaction.objects.create(
                    account=account,
                    transaction_type='deposit',
                    amount=amount,
                    balance_before=balance_before,
                    balance_after=account.balance
                )
            messages.success(request, f'Dépôt de {amount} XOF effectué avec succès.')
            return redirect('account_detail', account_id=account.id)
    else:
        form = DepositForm()
    return render(request, 'banking/deposit.html', {'form': form, 'account': account})

@login_required
def withdrawal(request, account_id):
    account = get_object_or_404(BankAccount, id=account_id, user=request.user)
    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if account.balance >= amount:
                with transaction.atomic():
                    balance_before = account.balance
                    account.balance -= amount
                    account.save()
                    Transaction.objects.create(
                        account=account,
                        transaction_type='withdrawal',
                        amount=amount,
                        balance_before=balance_before,
                        balance_after=account.balance
                    )
                messages.success(request, f'Retrait de {amount} XOF effectué avec succès.')
                return redirect('account_detail', account_id=account.id)
            else:
                messages.error(request, 'Solde insuffisant.')
    else:
        form = WithdrawalForm()
    return render(request, 'banking/withdrawal.html', {'form': form, 'account': account})

@login_required
def transfer(request, account_id):
    account = get_object_or_404(BankAccount, id=account_id, user=request.user)
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            recipient_account_number = form.cleaned_data['recipient_account']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data['description']
            try:
                recipient_account = BankAccount.objects.get(account_number=recipient_account_number)
                if account.balance >= amount:
                    with transaction.atomic():
                        # Debit sender
                        balance_before_sender = account.balance
                        account.balance -= amount
                        account.save()
                        Transaction.objects.create(
                            account=account,
                            transaction_type='transfer',
                            amount=amount,
                            balance_before=balance_before_sender,
                            balance_after=account.balance,
                            description=f'Virement vers {recipient_account_number}: {description}'
                        )
                        # Credit recipient
                        balance_before_recipient = recipient_account.balance
                        recipient_account.balance += amount
                        recipient_account.save()
                        Transaction.objects.create(
                            account=recipient_account,
                            transaction_type='transfer',
                            amount=amount,
                            balance_before=balance_before_recipient,
                            balance_after=recipient_account.balance,
                            description=f'Virement de {account.account_number}: {description}'
                        )
                    messages.success(request, f'Virement de {amount} XOF effectué avec succès.')
                    return redirect('account_detail', account_id=account.id)
                else:
                    messages.error(request, 'Solde insuffisant.')
            except BankAccount.DoesNotExist:
                messages.error(request, 'Compte destinataire introuvable.')
    else:
        form = TransferForm()
    return render(request, 'banking/transfer.html', {'form': form, 'account': account})
