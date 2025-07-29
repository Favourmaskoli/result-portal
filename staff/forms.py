from result.models import Result
from django import forms

class ResultsUploadForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = ['student', 'session', 'term', 'level',
                  'mark_obtained', 'subject']

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'term': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'mark_obtained': forms.NumberInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }