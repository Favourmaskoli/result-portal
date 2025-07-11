from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from student.models import Student

class StudentRegistrationForm(ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'address']

        def save(self, request=None, commit=True):
            if request is None or not request.user.is_authenticated:
                raise ValueError("User must be authenticated to save the student profile.")
            student = super().save(commit=False)
            student.user = request.user
            if commit:
                student.save()
            return student
