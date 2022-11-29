from django.shortcuts import render
from .models import teacher_details as td
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class teacherList(ListView):
    model = td
    success_url = reverse_lazy('teacher_list') 
