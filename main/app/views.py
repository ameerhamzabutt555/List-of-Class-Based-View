from django.http import HttpResponse
from .models import students
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import RedirectView, TemplateView
from .forms import feedback
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django import forms

class Student(DetailView):  #show all data students but one by one
    model = students

class ShowStudents(ListView):    #show all data students
    model = students

class StudentForm(CreateView):   #message form
    template_name = 'app/student_form.html'
    model = students
    fields = ['name','course','age']
    success_url = '/app/students/'

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'name'})
        form.fields['course'].widget=forms.TextInput(attrs={'class':'course'})
        form.fields['age'].widget=forms.TextInput(attrs={'class':'age'})
        return form

class StudentUpdate(UpdateView):   #message form
    template_name = 'app/student_update.html'
    model = students
    fields = ['name','course','age']
    success_url = '/app/students/'

    def get_form(self):
        form = super().get_form() #this method give access perent class
        form.fields['name'].widget=forms.TextInput(attrs={'class':'name'})
        form.fields['course'].widget=forms.TextInput(attrs={'class':'course'})
        form.fields['age'].widget=forms.TextInput(attrs={'class':'age'})
        return form


class MessagePage(FormView):   #message form
    template_name = 'app/feedback.html'
    form_class = feedback
    success_url = '/app/thanks/'

class ThanksPage(TemplateView):
    template_name = 'app/thanks.html'

class DeletPage(DeleteView):   #message form
    template_name = 'app/delet.html'
    model = students
    success_url = '/app/students/'