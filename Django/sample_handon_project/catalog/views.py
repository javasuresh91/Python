from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Book,BookInstance,Genre,Author,Language
from django.views.generic import CreateView,DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(req):
    return HttpResponse("hello")

def count_of_records(req):
    num_book = Book.objects.all().count()
    num_book_instance = BookInstance.objects.all().count()
    num_book_instance_avail = BookInstance.objects.filter(status__exact='a').count()
    
    contex = {'num_book':num_book,'num_book_instance':num_book_instance,'num_book_instance_avail':num_book_instance_avail}
    return  render(req,'catalog/index.html',context=contex)

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    #success_url='/catalog/home/' # BY default it will go to book_detail page by reverse mechanism
    
    
class BookDetailsView(DetailView):
    model = Book  
    
@login_required    
def user_auth_view(req):
    return render(req,'catalog/user_auth_function_view.html')
