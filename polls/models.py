from django.db import models

class Question(models.Model):
    """question model"""
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')

class choice(models.Model):
    """choice of question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=250)
    vote = models.IntegerField(default=0)
