from django.urls import path
from . import views


urlpatterns = [
    # Path for Accounts Model
    path('', views.home, name='supplier_index'),
    path('add/', views.supplier_entry, name='add_supplier'),
    path('<int:pk>/', views.view_supplier, name='view_supplier'),
    path('update/<int:pk>', views.update_supplier, name='update_supplier'),
    path('delete/<int:pk>', views.delete_supplier, name='delete_supplier')
]