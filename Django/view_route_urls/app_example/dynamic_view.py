from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse



articles = {
    
    "sport":"sport page",
    "finance": "finance page"    
    }

def dynamic_view_example(request,topic):
    # try and catch is used for handle 404 error, if the unknow key even by user which is not in the dictionary
    try :
        res = articles[topic]
        return HttpResponse(res)
    except:
        # HttpResponseNotFound("Invaild Input") Way one
        raise Http404("Invalid input due to iunknow value") # Way two

def add_view(request,num1,num2):
    print("comingdsds")
    return HttpResponse(num1+num2)

def num_page(req,num1):
    print("coming")
    page_number = list(articles.keys())
    topic = page_number[num1]
    print(topic)
    return HttpResponseRedirect('/app_example/'+topic)

def name_based_redirect(request):
    webpage = reverse("nameBasedRedirect")
    return HttpResponseRedirect(webpage)

def name_based_redirect_reach(request):
    return HttpResponse("Redirect success for named based")


