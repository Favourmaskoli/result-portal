# Generated by Django 5.2.3 on 2025-07-26 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_subject_mark_obtained_subject_total_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='mark_obtained',
        ),
    ]
