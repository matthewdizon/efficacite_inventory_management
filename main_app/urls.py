from django.urls import path
from . import views


urlpatterns = [
    path('accounts/login/', views.sign_in, name='sign_in'),
    path('create_account', views.create_account, name='create_account'),
    path('', views.home, name='index'),
    path('export_salesreport', views.export_salesreport, name='export_salesreport'),
    path('logout', views.logout_view, name='logout'),
]