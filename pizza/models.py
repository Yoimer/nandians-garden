from django.db import models

# Create your models here.

class Size(models.Model):
    title = models.CharField(max_length=100)

# this will help us show the size in forms and in the adming panel.
# __str__: works for any class NOT only classes in django
# and what it does is define what the object should look like
# when it's printed out to a screen. It applies when it's printed
# to a terminal or to a HTML.
def __str__(self):
    return self.title

class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    # this line creates a connection with to our size class
    # if one thing is deleted, we're also going to delete the corresponding object that has the relationship
    size = models.ForeignKey(Size, on_delete=models.CASCADE)