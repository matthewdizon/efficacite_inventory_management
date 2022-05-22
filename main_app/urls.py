from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('create_account', views.create_account, name='create_account'),
    path('home', views.home, name='index'),
    path('export_salesreport', views.export_salesreport, name='export_salesreport'),
]