from django.urls import path
from .views import index, create_student_profile, results, tasks, logout_view

app_name = 'student'
urlpatterns = [
    path('', index, name='student_index'),
    path('profile/', create_student_profile, name='student_profile'),
    path('results/', results, name='student_results'),
    path('tasks/', tasks, name='student_tasks'),
    path('logout/', logout_view, name='student_logout'),
]
