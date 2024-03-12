from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    confirm = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = "user"