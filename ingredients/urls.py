from django.urls import path
from . import views


urlpatterns = [
    # Path for Accounts Model
    path('', views.home, name='ingredient_index'),
    path('add/', views.add_ingredient, name='add_ingredient'),
    path('<int:pk>/', views.view_ingredient, name='view_ingredient'),
    path('update/<int:pk>/', views.update_ingredient, name='update_ingredient'),
    path('delete/<int:pk>', views.delete_ingredient, name='delete_ingredient'),
    path('batch_ingredient/<int:pk>/', views.batch_ingredient, name='batch_ingredient'),
    path('batch_updates', views.view_batch_updates, name='view_batch_updates'),
    path('send_mail', views.send_notification, name='send_notification'),
]