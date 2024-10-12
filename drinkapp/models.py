from django.db import models

# Create your models here.
class Drinkm(models.Model):
    name=models.CharField(max_length=25)
    description=models.TextField()
    def __str__(self):
        return self.name+ " "+self.description