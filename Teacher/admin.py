from django.contrib import admin
from . import models
# from .models import CompanyProblems


class teacher_Details_Admin(admin.ModelAdmin):
    list_display = ['user','Teacher_Name','department','position','Address','subject','Education','Experience','photo']

    exclude = ['user']
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(models.teacher_details, teacher_Details_Admin)

