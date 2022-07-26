from django.urls import path
from . import views

app_name = "classroom"


urlpatterns = [
    
    path('tempView/',views.MyTemplateView.as_view(),name="temp_view"),
    path('formView/',views.MyFormView.as_view(),name="form_view"),
    path('thankView/',views.MyThankView.as_view(),name="thank_view") ,
    path('createView/',views.TeacherCreateView.as_view(),name="create_view") ,
    path('listView/',views.TeacherListView.as_view(),name="list_view") ,
    path('detailView/<int:pk>',views.TeacherDetailView.as_view(),name="detail_view"),
    path('updateView/<int:pk>',views.TeacherUpdateView.as_view(),name="update_view"),
    path('deleteView/<int:pk>',views.TeacherDeleteView.as_view(),name="delete_view"),
    
]