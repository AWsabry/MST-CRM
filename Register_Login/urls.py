from django.urls import path
from Register_Login import views


app_name = 'Register_Login'

urlpatterns = [
    path('', views.index, name='index'),
]



