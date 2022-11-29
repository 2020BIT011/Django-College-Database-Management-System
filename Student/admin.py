from django.contrib import admin
from .models import Student_Details,Admission_Details,Marks,Feedback
# from .models import CompanyProblems


class Student_Details_Admin(admin.ModelAdmin):
    list_display = ['user','Student_Name','Reg_no','Address','Taluka','District','State','photo','pincode']

    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Student_Details, Student_Details_Admin)


class Admission_Details_Admin(admin.ModelAdmin):
    list_display = ['user','registration_No','S_name','Class_name','Branch','year','Date_of_Admission','Semester']

    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Admission_Details, Admission_Details_Admin)



class Marks_Admin(admin.ModelAdmin):
    list_display = ['user','Registration_No','Subject','marks','Semester','year']

    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Marks, Marks_Admin)



class Feedback_Admin(admin.ModelAdmin):
    list_display = ['user','Registration_no','date','subject','feedback']

    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Feedback, Feedback_Admin)




# class Teachers_Details_Admin(admin.ModelAdmin):
#     list_display = ['user','Teacher_Name','department','position','Address','subject','Education','Experience','photo']

#     exclude = ['user']
#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         obj.save()


# admin.site.register(Teacher_Details, Teachers_Details_Admin)

