from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL



class Vegetables(models.Model):
    user = models.ForeignKey(User, default=1, on_delete= models.CASCADE)
    name_veg = models.CharField()