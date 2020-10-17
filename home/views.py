from django.shortcuts import render,redirect
from home.models import *
from django.contrib import  messages
import  datetime
# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        
        ins = Post(title=title,body=body)
        ins.save()
        messages.success(request,"your detail are taken")
        print("imported contact")
    dataa = Post.objects.all()
    sorted_d = dataa.order_by("-time")
    context = {'dataa' :sorted_d}
    return render(request,'home.html',context)

def diaryseperate(request,slug):
    blog = Post.objects.filter(slug=slug).first()
    context = {'blog': blog}
    return render(request,'seperate.html',context)
def delete(request,slug):
    blog = Post.objects.filter(slug=slug).delete()
    messages.success(request,"deleted your recordes")

    return redirect(home)
def homesearch(request):
    if request.method == 'POST':
        date = request.GET['date']
        print(date)

    else:

        query = request.GET['query']
        
     
    
        searchtitle = Post.objects.filter(title__icontains=query)
        searchcontent = Post.objects.filter(body__icontains=query)
        searchtime= Post.objects.filter(time__icontains=query)
        searchr = searchtitle.union(searchcontent)
        search = searchr.union(searchtime)
        count = len(search)
        print(count,searchtime)

    context = {'blogs':search,'query':query,'count':count}
    
    return render(request,'search.html', context)


def s(request):
    return render(request,'s.html')

def search_date(request):
    if request.method == 'POST':
        date = request.POST['date']
        x = date.replace("/","-")
        lists = x.split("-")
        lists_sortedasformt = []
        lists_sortedasformt.append(lists[1])
        lists_sortedasformt.append(lists[0])
        lists_sortedasformt.append(lists[2])
        reversed_list = lists_sortedasformt[:: -1]
        reversed_sentence = "-".join(reversed_list)
        print( date, x,lists ,str(reversed_sentence))

    searchtime= Post.objects.filter(time__icontains= reversed_sentence)
    count = len(searchtime)
    print(searchtime)
    context = {'blogs':searchtime,'query':date,'count':count}
    
    return render(request,'search.html', context)