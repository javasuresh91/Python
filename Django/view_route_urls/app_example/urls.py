from django.urls import path,include
from . import views
from . import dynamic_view
from . import template_connect_view

urlpatterns = [
    path('one',views.simple_view,name="first_simple_view"),
    path('',views.simple_view,name="first_simple_view"),  
    
    path('<int:num1>/',dynamic_view.num_page), # Redirects
    
    path('<topic>/',dynamic_view.dynamic_view_example), # Dynamic View URL mapping
    path('<int:num1>/<int:num2>',dynamic_view.add_view), # Path Convertor in the Dynamic View URL mapping
    
    # Name Based re-direction
    path('name/entry/',dynamic_view.name_based_redirect),
    path('name/exit/',dynamic_view.name_based_redirect_reach,name="nameBasedRedirect"),
    
    path('template/connect',template_connect_view.template_view)
    
    ]


