
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class blog(models.Model):

    author=ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    desc=models.TextField(max_length=200)
    created_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    

