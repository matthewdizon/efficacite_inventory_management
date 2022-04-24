from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='order_index'),
    path('add/', views.add_order, name='add_order'),
    path('update/<int:pk>', views.update_order, name='update_order'),
    path('delete/<int:pk>', views.delete_order, name='delete_order'),
]