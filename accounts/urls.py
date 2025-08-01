from accounts import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login_redirect_path/', views.login_redirect_path, name='login_redirect_path'),
    # path('password_change_done', views.PasswordChange.as_view(), name='password_change_done'),
    path('password_change_done', TemplateView.as_view(template_name='registration/password_change_done.html'), name='password_change_done')
]