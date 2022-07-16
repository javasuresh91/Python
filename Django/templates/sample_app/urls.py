from django.urls import path
from . import views


#register the app namespace
app_name = 'my_app_name'

urlpatterns = [
    path("",views.example_template_view),
    path("variable/",views.variable_view),
    
    # URL names in template
    path("viewOne/",views.view_one, name="view_one"),
    path("viewTwo/",views.view_two, name="view_two"),
    
    # Temmplate inheritance
    path("inheritance/",views.view_inheritance, name="view_inheritance"),
    
    #Static FIle loading
    
    path("staticFile/",views.view_static_file)
    
    ]


