# Generated by Django 5.2.3 on 2025-07-26 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_rename_score_result_exam_score_result_test_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='exam_score',
        ),
        migrations.RemoveField(
            model_name='result',
            name='test_score',
        ),
        migrations.AddField(
            model_name='result',
            name='mark_obtained',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='result',
            name='date_taken',
            field=models.DateField(auto_now=True),
        ),
    ]
