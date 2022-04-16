from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='order_index'),
    path('add/', views.add_order, name='add_order'),
]