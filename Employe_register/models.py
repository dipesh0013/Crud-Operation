from django.db import models

# Create your models here.
class Position(models.Model):
    Title = models.CharField(max_length=40)

    def __str__(self):
        return self.Title



class Employee(models.Model):
    Fullname = models.CharField(max_length=30)
    Emp_code = models.CharField(max_length=4)
    Mobile = models.IntegerField()
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    def __str__(self):
        return self.Emp_code