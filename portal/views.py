from django.shortcuts import render

# Create your views here.

from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm

def login_view(request):



    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials.")
    return render(request, 'login.html')


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    students = Student.objects.all()
    form = StudentForm()

    return render(request, 'home.html', {'students': students, 'form': form})


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.subject = request.POST.get('subject')
        student.marks = request.POST.get('marks')
        student.save()
        return redirect('home')
    

    else:
        
        return render(request, 'edit_student.html', {'student': student})




def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('home')


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        subject = request.POST.get('subject', '').strip()
        marks = request.POST.get('marks', '').strip()

        if not name or not subject or not marks:
            messages.error(request, "All fields are required!")
            return redirect('home')

        try:
            marks = int(marks)
        except ValueError:
            messages.error(request, "Marks must be a number!")
            return redirect('home')

        
        try:
            student = Student.objects.get(name=name, subject=subject)
            student.marks += marks  
            student.save()
            messages.success(request, f"Updated {name}'s {subject} marks to {student.marks}.")
        except Student.DoesNotExist:
            Student.objects.create(name=name, subject=subject, marks=marks)
            messages.success(request, f"Added new student {name}.")

        return redirect('home')
    return redirect('home')





def delete_student(request, student_id):
    

    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('home')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')







def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        
        if not all([first_name, last_name, username, email, password]):
            messages.error(request, "All fields are required!")
            return redirect('signup')

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        messages.success(request, "Account created successfully. Please log in!")
        return redirect('login')
    return render(request, 'signup.html')






class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'reset_password.html'
    email_template_name = 'password_reset_email.html'
    success_url = '/reset_password_sent/'
