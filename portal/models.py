from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()

    class Meta:
        unique_together = ('name', 'subject')  # Avoid duplicate name-subject combos

    def __str__(self):
        return f"{self.name} - {self.subject}: {self.marks}"


from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'subject', 'marks']
