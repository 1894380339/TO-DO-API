from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return str(self.id)
        # return f'id:{self.id} - {self.username}'


class Task(models.Model):
    name_task = models.CharField(max_length=255, blank=False, null=False)
    Description_of_task = models.TextField(max_length=255, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_of_completion = models.DateTimeField()
    Status = models.BooleanField(choices=((False, "NEW"),(True, "COMPLETE")),default=False)
    Date_of_creation = models.DateTimeField(auto_now_add=True)
    Date_of_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)