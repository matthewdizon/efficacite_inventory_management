from django.urls import path
from . import views


urlpatterns = [
    # Path for Accounts Model
    path('', views.home, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('/<int:pk>', views.view_product, name='view_product'),
    path('update/', views.update_product, name='update_product'),

]