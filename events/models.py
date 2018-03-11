from django.db import models

# Create your models here.
class Events(models.Model):
	name= models.CharField(max_length=250)
	location= models.TextField(null= True)
	attendees= models.IntegerField(default=0)