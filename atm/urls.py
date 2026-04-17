from django.urls import path
from . import views

urlpatterns = [
    path('', views.atm_list, name='atm_list'),
    path('<int:atm_id>/restock/', views.atm_restock, name='atm_restock'),
]