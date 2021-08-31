from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(reques):
    return HttpResponse("hello,word,you're at the polls index")


def index2(request):
    context={'id':999999,'title':'site-web','text':'sssssssssssssss'}
    return render(request,'polls/index.html',context)    