from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, create_student_profile, results, tasks, logout_view, update_student

app_name = 'student'
urlpatterns = [
    path('', index, name='student_index'),
    path('profile/', create_student_profile, name='student_profile'),
    path('update_student/', update_student, name='update_profile'),
    path('results/', results, name='student_results'),
    path('tasks/', tasks, name='student_tasks'),
    path('logout/', logout_view, name='student_logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
