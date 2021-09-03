from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from polls import  models


def book(request):
   books = models.Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10",cre="2021-08-31",creator='hua') 
   return HttpResponse("SUCCESS")


def index(reques):
    return HttpResponse("hello,word,you're at the polls index")


def index2(request):
    context={'id':999999,'title':'site-web','text':'sssssssssssssss'}
    return render(request,'polls/index.html',context)    