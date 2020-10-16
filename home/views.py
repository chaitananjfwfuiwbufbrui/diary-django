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
    """   if len(query) > 50:
        searchr = Post.objects.none()
    else:
                
        searchtitle = Post.objects.filter(title__icontains=query)
        searchcontent = Post.objects.filter(body__icontains=query)
       # searchtime = Post.objects.filter(time=datetime.date(query))
        searchr = searchtitle.union(searchcontent)
        print(searchtitle,searchcontent)
    count = len(searchr)
    """
    searchtitle = Post.objects.filter(title__icontains=query)
    searchcontent = Post.objects.filter(body__icontains=query)
    searchtime= Post.objects.filter(time__icontains=query)
    searchr = searchtitle.union(searchcontent)
    search = searchr.union(searchtime)
    count = len(search)
    print(count,searchtime)

    context = {'blogs':search,'query':query,'count':count}
    
    return render(request,'search.html', context)

"""#
def search(request):
    query = request.GET['query']
    if len(query) > 50:
        searchr = Post.objects.none()
    else:
                
        searchtitle = Post.objects.filter(title__icontains=query)
        searchcontent = Post.objects.filter(content__icontains=query)
        searchr = searchtitle.union(searchcontent)

    if searchr.count() == 0:
    
    
        context = {'blogs':searchr}



    return render(request,'search.html', context)
"""
def s(request):
    return render(request,'s.html')