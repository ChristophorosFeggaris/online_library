from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('A', 'Available'),
        ('I', 'Issue')
    ]
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')

    def __str__(self):
        return self.title
