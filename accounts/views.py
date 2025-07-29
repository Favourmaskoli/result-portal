from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class PasswordChange(UpdateView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'registration/password_change_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
def login_redirect_path(request):
    """Redirect a user based on permission"""
    user = request.user
    if (user.is_staff or user.is_superuser):
        return redirect('staff:dashboard')
    else:
        return redirect('student:student_index')