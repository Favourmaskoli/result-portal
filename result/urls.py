from django.urls import path
from payment import views

urlpatterns = [
    path('', views.home, name='home')
]