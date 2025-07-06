from django.db import models
from subject.models import Subject

class Result(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='results')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='results')
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date_taken = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.score}"

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        ordering = ['-date_taken', 'student__last_name']
