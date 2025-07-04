from notifications import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="notify")
]