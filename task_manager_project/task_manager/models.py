from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('high', 'Высокий'),
        ('medium', 'Средний'),
        ('low', 'Низкий'),
    )
    STATUS_CHOICES = (
        ('open', 'Открыта'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
        ('closed', 'Закрыта'),
    )

    title = models.CharField(max_length=250)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    note = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='open')
    creation_date = models.DateTimeField(default=timezone.now)

    objects = models.Manager()

    def __str__(self):
        return self.title

# qwe123