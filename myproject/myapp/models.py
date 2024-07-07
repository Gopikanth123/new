from django.db import models
from django.utils import timezone

class Registration(models.Model):
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    course_name = models.CharField(max_length=255)
    testimonial = models.TextField()
    accept = models.BooleanField(default=False)
    action_by = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    email = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='testimonials', db_column='email_id')

    def __str__(self):
        return f"Testimonial for {self.course_name} by {self.email}"

class CourseEnrollment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=30)
    user_mobile = models.CharField(max_length=11)
    course_name = models.CharField(max_length=50)
    testimonial = models.CharField(max_length=200, null=True, blank=True)
    course_completion = models.CharField(max_length=1)
    testimonial_status = models.CharField(max_length=1, null=True, blank=True)

    class Meta:
        db_table = 'course_enrollments'

    def __str__(self):
        return f"{self.user_name} - {self.course_name}"
