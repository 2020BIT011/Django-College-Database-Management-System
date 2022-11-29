from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class teacher_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    Teacher_Name = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    
    Education = models.CharField(max_length=50)
    Experience = models.CharField(max_length=50)

    photo = models.ImageField(upload_to="media/img")
    
    def __str__(self):
        return '%s -%s' % (self.Teacher_Name,self.position)
    
class Meta:
        verbose_name = "Teacher Information"
        verbose_name_plural = "Teacher Informations"

#'user','Teacher_Name','department','position','Address','subject','Education','Experience','photo'