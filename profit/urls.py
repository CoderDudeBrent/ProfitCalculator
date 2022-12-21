from django.urls import path

from . import views

urlpatterns = [
    path('', views.profit, name="profit"),
    path('calculate_profit/', views.calculate_profit, name='calculate_profit'),
]
