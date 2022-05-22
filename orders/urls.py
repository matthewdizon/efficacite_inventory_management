from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='order_index'),
    path('add/', views.OrderAddView.as_view(), name='add_order'),
    path('update/<int:pk>', views.update_order, name='update_order'),
    path('delete/<int:pk>', views.delete_order, name='delete_order'),
]