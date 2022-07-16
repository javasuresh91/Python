from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def example_template_view(req):
    return render(req,'sample_app/example.html')
    
def variable_view(req):
    my_var = {'first_name':'SuReHD',"some_list":[1,2,3],"some_dict":{"data":"6598"},"user_logged_in":True}
    return render(req,'sample_app/variable.html',context=my_var)

def view_one(req):
    return render(req,'sample_app/view_one.html')

def view_two(req):
    return render(req,'sample_app/view_two.html')


def view_inheritance(req):
    return render(req,'sample_app/child.html')

def view_static_file(req):
    return render(req,'sample_app/view_static_file.html')