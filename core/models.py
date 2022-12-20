from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.__str__()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_image')
    captio = models.TextField()
    created_at = models.DateTimeField(default=datetime)
    no_of_like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user

