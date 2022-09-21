from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null = True, blank = True)
    updated = models.DateTimeField(auto_now= True) #every time a save method is called on this attribute, the field is updated with the timestamp 
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.body[0:50]

        