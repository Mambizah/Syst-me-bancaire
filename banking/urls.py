from django.urls import path
from . import views

urlpatterns = [
    path('account/<int:account_id>/', views.account_detail, name='account_detail'),
    path('account/<int:account_id>/deposit/', views.deposit, name='deposit'),
    path('account/<int:account_id>/withdrawal/', views.withdrawal, name='withdrawal'),
    path('account/<int:account_id>/transfer/', views.transfer, name='transfer'),
]