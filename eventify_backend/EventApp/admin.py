from django.contrib import admin
from .models import User, Event, Post, Comment, Photo, EventFavorite

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(EventFavorite)

