from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import CustomUserCreationForm
from banking.models import BankAccount

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                # Create default current account
                BankAccount.objects.create(user=user, account_type='current')
                login(request, user)
                messages.success(request, 'Inscription réussie ! Votre profil est maintenant actif.')
                return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'profile'
            return redirect(next_url)
        else:
            messages.error(request, 'Identifiants invalides.')
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Déconnexion réussie.')
    return redirect('login')

@login_required
def profile(request):
    accounts = BankAccount.objects.filter(user=request.user, is_active=True)
    total_balance = sum([account.balance for account in accounts]) if accounts else 0
    return render(request, 'accounts/profile.html', {
        'accounts': accounts,
        'total_balance': total_balance
    })

@login_required
def dashboard(request):
    accounts = BankAccount.objects.filter(user=request.user, is_active=True)
    return render(request, 'accounts/dashboard.html', {'accounts': accounts})
