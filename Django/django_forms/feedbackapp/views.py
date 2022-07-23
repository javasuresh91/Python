from django.shortcuts import render,redirect
from .dj_form import ReviewForm;
from .widgets_form import WidgetsForm

from django.urls import reverse

def rental_review(req):
    
    if req.method == 'POST':
        form = ReviewForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse("feed:thank_view"))
    else:
        form = ReviewForm()
    return render(req, "feedbackapp/rental_review.html",context={"form":form})

def thank_you(req):
    return render(req,"feedbackapp/thank_you.html")

def template_render(req):
    if req.method == 'POST':
        form = ReviewForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse("feed:template_render"))
    else:
        form = ReviewForm()
        
    return render(req, "feedbackapp/template_rendering.html",context={"form":form})

def widget_validation(req):
    form = WidgetsForm()
    return render(req,"feedbackapp/widgets_validation_styling.html",context={"form":form})
