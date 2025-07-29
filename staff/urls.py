from django.urls import path
from staff.views import staff_dashboard, upload_result

app_name = 'staff'

urlpatterns = [
    path('dashboard/', staff_dashboard, name='dashboard'),
    path('upload_result', upload_result, name='upload_result')
]