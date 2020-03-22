from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name = 'profile')
    bio = models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
class Case(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    describe =  models.TextField(default='qwerty')
    caseimg = models.ImageField(upload_to='images',)
    img1 = models.ImageField(upload_to='images',)
    nam1 = models.CharField(max_length=40,default='qwerty')
    img2 = models.ImageField(upload_to='images', )
    nam2 = models.CharField(max_length=40,default='qwerty')
    img3 = models.ImageField(upload_to='images', )
    nam3 = models.CharField(max_length=40,default='qwerty')
    img4 = models.ImageField(upload_to='images',)
    nam4 = models.CharField(max_length=40,default='qwerty')
    img5 = models.ImageField(upload_to='images',)
    nam5 = models.CharField(max_length=40,default='qwerty')
    img6 = models.ImageField(upload_to='images',)
    nam6 = models.CharField(max_length=40,default='qwerty')
class Items(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(Profile, on_delete = models.CASCADE)
    mydate = models.DateTimeField(default=datetime.now()+timedelta(days=90))
    def yearpublished(self):
        return self.mydate.strftime("%d/%m/%y")
