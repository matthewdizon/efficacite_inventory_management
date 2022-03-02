from django.urls import path
from . import views


urlpatterns = [
    # Path for Accounts Model
    path('', views.home, name='index'),
    # path('add/', views.add_product, name='add_product'),
    path('<int:pk>/', views.view_ingredient, name='view_ingredient'),
    # path('update/<int:pk>', views.update_product, name='update_product'),
    # path('delete/<int:pk>', views.delete_product, name='delete_product')
]