from django.shortcuts import render
from .models import Student_Details,Admission_Details,Marks,Feedback
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class StudentList(ListView):
    model = Student_Details
    success_url = reverse_lazy('student_list') 



class StudentListCreate(CreateView):
    model = Student_Details
    fields = ['user','Student_Name','Reg_no','Address','Taluka','District','State','photo','pincode']
    
    success_url = reverse_lazy('student_list')


class StudentListUpdate(UpdateView):
    model = Student_Details
    fields = ['user','Student_Name','Reg_no','Address','Taluka','District','State','photo','pincode']
    success_url = reverse_lazy('student_list')


class StudentListDelete(DeleteView):
    model = Student_Details
    success_url = reverse_lazy('student_list')

class AdmissionList(ListView):
    model = Admission_Details
    success_url = reverse_lazy('Admission_list') 


# class TeacherList(ListView):
#     model = Teacher_Details
#     success_url = reverse_lazy('Teacher_list') 

class MarksList(ListView):
    model = Marks
    success_url = reverse_lazy('Marks_list')     


class FeedbackList(ListView):
    model = Feedback
    success_url = reverse_lazy('Feedback_list')  

def view_record(request):

    stud_record = Student_Details.objects.all()
    Addmission_record = Admission_Details.objects.all()
    Marks_record = Marks.objects.all()
    feedback_record = Feedback.objects.all()
    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'record.html',{'stud12':stud_record,'Add12':Addmission_record,'mark12':Marks_record,'feed12':feedback_record})


def view_Student_Data(request):
    
    stud_record = Student_Details.objects.all()
    return render(request,'student_data.html',{'stud12':stud_record})


def view_Addmission_Data(request):
    
    Addmission_record = Admission_Details.objects.all()
    return render(request,'addmission_Data.html',{'Add12':Addmission_record})
