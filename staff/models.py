from django.db import models
from django.contrib.auth.models import User
from school.models import School

def get_default_school():
    return School.objects.first() if School.objects.exists() else None  

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='staff_members', editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=50)
    date_hired = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.school_id:
            self.school = get_default_school()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.position}"

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"
        ordering = ['user__last_name', 'user__first_name']
