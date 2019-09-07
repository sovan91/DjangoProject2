from django.db import models
# user model is being created here with some properties
class Users(models.Model):
    Name = models.CharField(max_length=256)
    Email = models.EmailField(max_length=256,unique=True)



