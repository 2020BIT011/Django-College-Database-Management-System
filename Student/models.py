from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Student_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    Student_Name = models.CharField(max_length=30)
    Reg_no = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Taluka = models.CharField(max_length=30)
    District = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="media/img")
    pincode = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s -%s' % (self.Student_Name, self.Reg_no)
    
class Meta:
        verbose_name = "Student Information"
        verbose_name_plural = "Student Informations"
    
#'user','Student_Name','Reg_no','Address','Taluka','District','State','photo','pincode'

class Admission_Details(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,blank=True,
    #                          blank=True, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    registration_No = models.ForeignKey(Student_Details, on_delete=models.CASCADE)
    S_name = models.CharField(max_length=30)
    Class_name = models.CharField(max_length=30)
    Branch = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    Date_of_Admission = models.DateField()
    Semester = models.CharField(max_length=30)
    #
    def __str__(self):
        return '%s' % (self.registration_No)

#'user','Reg_No','S_name','Class_name','Branch','year','Date_of_Admission','Semester'

class Meta:
        verbose_name = "Admission Information"
        verbose_name_plural = "Admission Informations"


class Marks(models.Model):
   

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    Registration_No = models.ForeignKey(Student_Details, on_delete=models.CASCADE)   
    Subject = models.CharField(max_length=30)
    marks = models.CharField(max_length=30)   
    Semester = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s' % (self.Registration_No)

#'user','Registration_No','Subject','marks','Semester','year'
class Meta:
        verbose_name = "marks Information"
        verbose_name_plural = "marks Informations"


class Feedback(models.Model):
       

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    Registration_no = models.ForeignKey(Marks, on_delete=models.CASCADE)   
    date = models.DateField()   
    subject = models.CharField(max_length=30)
    feedback = models.TextField(max_length=1000)
    
    def __str__(self):
        return '%s' % (self.Registration_no)

class Meta:
        verbose_name = "Feedback Information"
        verbose_name_plural = "Feedback Informations"
        
        
#'user','Registration_no','date','subject','feedback'


# class Teacher_Details(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
#     Teacher_Name = models.CharField(max_length=30)
#     department = models.CharField(max_length=50)
#     position = models.CharField(max_length=30)
#     subject = models.CharField(max_length=50)
#     Address = models.CharField(max_length=50)
    
#     Education = models.CharField(max_length=50)
#     Experience = models.CharField(max_length=50)

#     photo = models.ImageField(upload_to="media/img")
    
#     def __str__(self):
#         return '%s -%s' % (self.Teacher_Name,self.position)
    
# class Meta:
#         verbose_name = "Teacher Information"
#         verbose_name_plural = "Teacher Informations"

#'user','Teacher_Name','department','position','Address','subject','Education','Experience','photo'