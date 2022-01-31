from django.db import models

# Create your models here.
class Breed(models.Model):
    
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=255)
    friendliness = models.IntegerField()
    train_ability = models.IntegerField()
    shedding_amount = models.IntegerField()
    exercise_needs = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'
    
class Dog(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, default='')
    gender = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.id}'