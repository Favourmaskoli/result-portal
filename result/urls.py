from django.urls import path
from result.views import index


app_name = 'result'
urlpatterns = [
    path('', index, name='index'),
]
