from django.urls import path
from . import views


app_name = 'organizations_and_services'

urlpatterns = [
    path('organizations_home', views.organizations_home, name='organizations_home'),
]



