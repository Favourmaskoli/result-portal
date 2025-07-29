from django.db import models
from django.contrib.auth.models import User
from school.models import School

def get_default_school():
    return School.objects.first() if School.objects.exists() else None

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    image = models.ImageField(upload_to='student/profile', default=('images/default.png'))
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students', editable=False)
    first_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.school_id:
            self.school = get_default_school()
        super().save(*args, **kwargs)

    @property
    def is_student(self):
        return True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['last_name', 'first_name']
