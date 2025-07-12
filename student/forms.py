from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from student.models import Student

class StudentProfileForm(ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'date_of_birth', 'phone_number', 'address']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        def save(self, request=None, commit=True):
            if request is None or not request.user.is_authenticated:
                raise ValueError("User must be authenticated to save the student profile.")
            student = super().save(commit=False)
            student.user = request.user
            if commit:
                student.save()
            return student
