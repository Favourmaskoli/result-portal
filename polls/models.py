from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    """question model"""
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """return a string rep"""
        return self.question_text
    def was_pub_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class choice(models.Model):
    """choice of question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


