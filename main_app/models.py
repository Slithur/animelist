from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.



class Anime(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'anime_id': self.id})


  


