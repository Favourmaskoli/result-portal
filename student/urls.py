from django.urls import path
from .views import index, profile, results, tasks, logout_view, result_details

app_name = 'student'
urlpatterns = [
    path('', index, name='student_index'),
    path('profile/', profile, name='student_profile'),
    path('results/', results, name='student_results'),
    path('tasks/', tasks, name='student_tasks'),
    path('logout/', logout_view, name='student_logout'),
    path('result/', result_details, name='student_result_details'),
]
