from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy
# Create your views here.
class Home(TemplateView):
    template_name='app/home.html'

class Schoollist(ListView):
    model=School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class schoolupdate(UpdateView):
    model=School
    fields='__all__'

class schooldelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('school_list')