from django.shortcuts import render
from django.views.generic  import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models

# Create your views here.
class MyTemplateView(TemplateView):
    template_name = 'cbv/cbv_template_view.html'

class MyThankView(TemplateView):
    template_name = 'cbv/thank_you.html'


class MyFormView(FormView):
    form_class = forms.ContactForm
    template_name = 'cbv/contact.html'
    
    #After successfull Form submit
    success_url='/classroom/thankView/' #this not template url, it shoud be raw template
    
    #What to do with folrm data
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class TeacherCreateView(CreateView):
    model =  models.Teacher
    fields = ["first_name","last_name"]
    #If you want all fields to show, just simply say fields="__all__"
    
    #After successfull Form submit
    success_url='/classroom/thankView/' #this not template url, it shoud be raw template
    #success_url = reverse_lazy('classroom:thank_view') This is used the template naming
    
class TeacherListView(ListView):
    model = models.Teacher
    #context_object_name = "teacher_list"    so you can access the list of data in the teacher_list in the template instead of object_list
    #query_set = Teacher.objects.all() This is default query we can change it as we like
    
class TeacherDetailView(DetailView):
    model = models.Teacher 
    # By default , it accepts the Primary Key as input and give the model object to the template

class TeacherUpdateView(UpdateView):
    model = models.Teacher
    fields=["last_name","subject"] # If we need to update all feilds, just give feilds="__all__"    
    success_url = reverse_lazy('classroom:thank_view')
 
class TeacherDeleteView(DeleteView):
    model = models.Teacher    
    success_url = reverse_lazy('classroom:thank_view')