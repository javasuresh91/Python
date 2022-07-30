from django.urls import path
from . import views

urlpatterns=[
path ('',views.index,name="index"),
path ('home/',views.count_of_records,name="home")    ,
path ('addBook/',views.BookCreateView.as_view(),name="bookCreate")    ,
path ('book/<int:pk>',views.BookDetailsView.as_view(),name="book_details")    ,
path ('userAuthCheck/',views.user_auth_view,name="userAuth")
]