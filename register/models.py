from django.db import models
from django.urls import reverse
# import datetime
import django


class Saloon(models.Model):
    name=models.CharField(max_length=250)
    ad_first=models.CharField(max_length=250)
    ad_second=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    pincode=models.CharField(max_length=250)
    image=models.ImageField(blank=True,upload_to="profile_pics")
    password=models.CharField(max_length=250)
    email=models.EmailField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("admin")
    


class Post(models.Model):
    saloon=models.ForeignKey(Saloon,related_name="saloon_post",on_delete=models.PROTECT)
    title=models.CharField(max_length=250)
    type_post=models.IntegerField()
    image=models.ImageField(blank=True,upload_to="profile_pics")
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("admin")




    
class UserSaloon(models.Model):
    name=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    country=models.CharField(max_length=250)
    image=models.ImageField(blank=True,upload_to="profile_pics")
    password=models.CharField(max_length=250)
    email=models.EmailField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("admin")
    
class Like(models.Model):
    post=models.ForeignKey(Post,related_name="post_like",on_delete=models.PROTECT)
    user=models.ForeignKey(UserSaloon,related_name="user_like",on_delete=models.PROTECT)
    time=models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse("admin")


class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="post_comment",on_delete=models.PROTECT)
    user=models.ForeignKey(UserSaloon,related_name="user_comment",on_delete=models.PROTECT)
    time=models.DateTimeField(default=django.utils.timezone.now)
    comment=models.TextField()

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse("admin")


class Subscribed(models.Model):
    saloon=models.ForeignKey(Saloon,related_name="saloon_subscribe",on_delete=models.PROTECT)
    user=models.ForeignKey(UserSaloon,related_name="user_subscribe",on_delete=models.PROTECT)
    time=models.DateTimeField(default=django.utils.timezone.now)
    # comment=models.TextField()

    def __str__(self):
        return self.saloon

    def get_absolute_url(self):
        return reverse("admin")




class Files(models.Model):
    # file=models.FileField(blank=True,upload_to="saloon")
    image=models.ImageField(blank=True,upload_to="profile_pics")
    def __str__(self):
        return self.image.name