from django.contrib import admin
from .models import ATM, ATMRestock

@admin.register(ATM)
class ATMAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'status', 'cash_available', 'max_withdrawal')
    search_fields = ('name', 'city', 'address')
    list_filter = ('status', 'city')

@admin.register(ATMRestock)
class ATMRestockAdmin(admin.ModelAdmin):
    list_display = ('atm', 'amount_added', 'restocked_by', 'restocked_at')
    search_fields = ('atm__name', 'restocked_by')
    list_filter = ('restocked_at',)
