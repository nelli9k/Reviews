from django.db import models

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.username} - {self.text} at {self.date}"