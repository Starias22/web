from django.db import models
# Create your models here.

#Course model
class Course(models.Model):

    name=models.CharField(max_length=100)# the name of the course
    #lastUpdate=models.DateField()# the date of last update
    isGiven=models.BooleanField()# if the course is already given or not
    #aded field(s)
    teacher=models.TextField()#the name of the teacher
    def __str__(self):
        return self.name[:10]