from django import forms
from .models import Student
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'subject', 'marks']



class CustomPasswordResetForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        if not User.objects.filter(username=username, email=email).exists():
            raise forms.ValidationError(
                "No user found with this username and email address."
            )
        return cleaned_data
