from django.db import models
from subject.models import Subject
from school.models import School, Level, Term, Session

class Result(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='results')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='results', null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='results', null=True, blank=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='results', null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='results', null=True, blank=True)
    mark_obtained = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    date_taken = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.mark_obtained} - {self.term}"
    
    def percentage_score(self):
        if self.subject.total_marks:
            return round((self.mark_obtained / self.subject.total_marks) * 100, 2)
        return 0
    
    def grade(self):
        percentage_score = self.percentage_score()
        if percentage_score >= 70:
            return "A", "Excellent"
        if percentage_score >= 60:
            return "B", "Very Good"
        if percentage_score >= 50:
            return "C", "Good"
        if percentage_score >= 45:
            return "D", "Fair"
        if percentage_score >= 40:
            return "E", "Pass"
        else:
            return "F", "Fail"

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        ordering = ['-date_taken', 'student__last_name']
