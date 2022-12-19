from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.__str__()
