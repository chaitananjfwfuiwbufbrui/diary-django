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
    context = {'dataa' :dataa}
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
    query = request.GET['query']
    print(query)
    if len(query) > 50:
        searchr = Post.objects.none()
    else:
                
        searchtitle = Post.objects.filter(title=query)
        searchcontent = Post.objects.filter(body__icontains=query)
        searchtime = Post.objects.filter(time=datetime.date(query))
        searchr = searchtitle.union(searchtime)

    count = len(searchr)
    


    context = {'blogs':searchr,'query':query,'count':count}
    
    return render(request,'search.html', context)
