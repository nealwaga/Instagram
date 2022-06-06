from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create models here
# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
#     profile_pic = CloudinaryField('profile_pic', null=True)
#     first_name = models.CharField(max_length=200, null=True, blank=True)
#     last_name = models.CharField(max_length=200, null=True, blank=True)
#     pronouns = models.CharField(max_length=10, null=True, blank=True)
#     bio = models.TextField(max_length=200, null=True, blank=True)
#     website = models.URLField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return self.bio

#     #search
#     @classmethod
#     def search_by_user(cls,search_term):
#         instauser = cls.objects.filter(user__icontains=search_term)
#         return instauser

# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)