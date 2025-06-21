from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView
urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout', views.logout, name="logout"),
    path('home/', views.home, name='home'),



    path('add/', views.add_student, name='add_student'),
    # path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),

    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    # path('signup/', views.signup_view, name='signup'),
    path('signup/', views.signup, name='signup'),


    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='reset_password.html'
    ), name='reset_password'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='reset_password_sent.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset_password_confirm.html'
    ), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset_password_complete.html'
    ), name='password_reset_complete'),
    path('reset_password/', CustomPasswordResetView.as_view(), name='reset_password'),

]



