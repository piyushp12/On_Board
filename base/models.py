import math
from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.forms import HiddenInput

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_number = models.IntegerField(blank=True,null=True)
    Physics= models.CharField(max_length=20)
    Chemistry = models.CharField(max_length=20)
    Biology= models.CharField(max_length=20)
    Mathematics= models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "12 Class Science"

class Studentone(models.Model):
    name = models.CharField(max_length=20)
    roll_number = models.IntegerField(blank=True,null=True,unique=True)
    Physics= models.CharField(max_length=20)
    ChemistryChemistry = models.CharField(max_length=20)
    Biology= models.CharField(max_length=20)
    Mathematics= models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "11 Class Science"

class Studenttwo(models.Model):
    name = models.CharField(max_length=20)
    roll_number = models.IntegerField(blank=True,null=True)
    Accountancy= models.CharField(max_length=20)
    Business = models.CharField(max_length=20)
    Economics = models.CharField(max_length=20)
    English = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "12 Class Commerce"


class Studentthree(models.Model):
    name = models.CharField(max_length=20)
    roll_number = models.IntegerField(blank=True,null=True)
    Accountancy= models.CharField(max_length=20)
    Business = models.CharField(max_length=20)
    Economics = models.CharField(max_length=20)
    English = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "11 Class Commerce"


class Studentfour(models.Model):
    name = models.CharField(max_length=20)
    roll_number = models.IntegerField(blank=True,null=True)
    History= models.CharField(max_length=20)
    hindi = models.CharField(max_length=20)
    Sociology = models.CharField(max_length=20)
    Economics = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "12 Class Arts"

class Studentfive(models.Model):
    name = models.CharField(max_length=20)
    roll_number = models.IntegerField(blank=True,null=True)
    History = models.CharField(max_length=20)
    hindi = models.CharField(max_length=20)
    Sociology= models.CharField(max_length=20)
    Economics= models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "11 Class Arts"


#-----------------------------------------#
# class Name(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

#"Name",on_delete=models.CASCADE,default=1,null=True,blank=True

