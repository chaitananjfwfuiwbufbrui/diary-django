from django.db import models
from django.db.models.signals import pre_save
from diary1.utils import unique_slug_generator
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.title
def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator,sender=Post)