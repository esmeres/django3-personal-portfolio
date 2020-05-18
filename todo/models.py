from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted= models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    #one to many relationship, establish that every to do for every user
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    #making the entry in the database inside admin page more readable