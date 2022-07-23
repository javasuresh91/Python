from django.urls import path
from . import views

app_name="feed"

urlpatterns=[
    path('rental_view/',views.rental_review,name="ren_view"),
    path('thanks_view/',views.thank_you,name="thank_view"),
path('template_render',views.template_render,name="template_render")  ,
path('widget_valid/',views.widget_validation,name="widget_validation")  ,  
]