from django.db import models

# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=30)
     content = models.TextField(max_length=1000)
     image = models.ImageField(upload_to="posts/")
     def __str__(self):
        return str(self.title)
