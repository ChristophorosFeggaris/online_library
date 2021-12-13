from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('A', 'Available'),
        ('I', 'Issue')
    ]
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    book_pic = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')

    def __str__(self):
        return self.title

    @property
    def bookpic_url(self):
        if self.book_pic and hasattr(self.book_pic, 'url'):
            return self.book_pic.url
        else:
            return "/static/images/default-image.png"
    """
    class Meta:
        unique_together = ('slug', 'category')
        ordering = ['-timestamp']
    """
