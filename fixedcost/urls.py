from django.urls import path

from . import views

urlpatterns = [
    path('', views.fixedcost, name="fixedcost"),
    path('calculate_cost/', views.calculate_cost, name='calculate_cost'),
]
