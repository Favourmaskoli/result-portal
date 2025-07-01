from django.urls import path
from schools import views

urlpatterns = [
    path('', views.home, name='home')
]