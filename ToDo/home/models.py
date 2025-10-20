from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length= 100)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.created}'
    
