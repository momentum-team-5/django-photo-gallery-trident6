from django.contrib import admin
from .models import Gallery, Photo, Comment

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Photo)
admin.site.register(Comment)
