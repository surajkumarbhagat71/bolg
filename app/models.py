from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    description = models.TextField()
    CHOICE = (('PUBLIC','PUBLIC'),('PRIVATE','PRIVATE'))
    status = models.CharField(choices=CHOICE , max_length=200)

    def __str__(self):
        return self.title





