from django.db import models
from datetime import datetime

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
        ordering = ['name']

class Level(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Level"
        verbose_name_plural = "Levels"
        ordering = ['name']

class Term(models.Model):
    terms = (
        ('First', 'First Term'),
        ('Second', 'Second Term'),
        ('Third', 'Third Term'),
    )
    name = models.CharField(max_length=20, choices=terms)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

def get_sessions(start_year):
    current_year = datetime.now().year
    years = list(range(start_year, current_year + 1))
    return [((f"{y}/{y+1}"), f"{y}/{y+1}") for y in years]

school = School.objects.first()
class Session(models.Model):
    session_year = models.CharField(max_length=9, choices=get_sessions(school.established_date.year), unique=True)

    def __str__(self):
        return self.session_year
