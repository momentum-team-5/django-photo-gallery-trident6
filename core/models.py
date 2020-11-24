from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Gallery(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='gallerys')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    is_private = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} {self.date} {self.is_private}"

class Photo(models.Model):
    gallery = models.ForeignKey(to=Gallery, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    alt_text = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/gallery_images/', null=True)
    date = models.DateField(auto_now=True)
    default = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.gallery} {self.title} {self.description} {self.alt_text} {self.image} {self.date}"

class Comment(models.Model):
    photo = models.ForeignKey(to=Photo, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')    
    text = models.TextField(blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.photo} {self.user} {self.text} {self.date}"
