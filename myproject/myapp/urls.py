from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('check_database/', check_database, name='check_database'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('notifications/', notifications, name='notifications'),
    path('testimonials/', testimonials, name='testimonials'),
    path('manage_members/', manage_members, name='manage_members'),
    path('manage_courses/', manage_courses, name='manage_courses'),
    path('approve_testimonial/<int:testimonial_id>/', approve_testimonial, name='approve_testimonial'),
    path('reject_testimonial/<int:testimonial_id>/', reject_testimonial, name='reject_testimonial'),
    # path('feedback/', feedback, name='feedback'),
]
