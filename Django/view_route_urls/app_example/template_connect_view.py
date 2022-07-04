from django.shortcuts import render

def template_view(req):
    return render(req, 'example.html')

