from django.urls import path

from . import views

urlpatterns = [
    path('', views.variablecost, name="variablecost"),
    path('calculate_v_cost/', views.calculate_v_cost, name='calculate_v_cost'),
]
