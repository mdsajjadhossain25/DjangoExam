from django.db import models

# Create your models here.
size_choices = (
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
)
choices_list =(
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
)
gender_choices = (
    ("male", "male"),
    ("female", "female"),
    ("none","none"),
)

class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, choices=size_choices)
    friendliness = models.CharField(max_length=10, choices=choices_list)
    trainability = models.CharField(max_length=10, choices=choices_list)
    sheddingamout = models.CharField(max_length=10, choices=choices_list)
    exerciseneeds = models.CharField(max_length=10, choices=choices_list)
    
    def __str__(self):
        return self.name
    
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=gender_choices)
    color = models.CharField(max_length=20)
    favoritefood = models.CharField(max_length=30)
    favoritetoy = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
    
    