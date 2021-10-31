from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=500)
    profile_photo = CloudinaryField('image')
    

    def __str__(self):
        return self.user.username 

    def save_profile(self):
        self.save()

    def update_profile(self,):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile