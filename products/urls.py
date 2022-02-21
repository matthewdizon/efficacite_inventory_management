from django.urls import path
from . import views


urlpatterns = [
    # Path for Accounts Model
    path('', views.home, name='index'),
]