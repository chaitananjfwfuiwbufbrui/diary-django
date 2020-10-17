from django.shortcuts import render,redirect
from home.models import *
from django.contrib import  messages
import  datetime
from  django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    userrs = request.user
    x = "AnonymousUser"
    print(userrs)
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        users = request.POST['user']
        
        ins = Post(title=title,body=body,user=users)
        ins.save()
        messages.success(request,"your detail are taken")
        print("imported contact")
    if userrs == x:
        dataa = Post.objects.filter(user=userrs)
        sorted_d = dataa.order_by("-time")
        context = {'dataa' :sorted_d}
    else:
        dataa = Post.objects.filter(user=userrs)
        sorted_d = dataa.order_by("-time")
        count= len(sorted_d)
                
        print(count)
        context = {'dataa' :sorted_d,'count':count}


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

#api
def handleauth(request):
    if request.method == 'POST':
       user = request.POST['signupuser'] 
       email = request.POST['signupemail']
       signupfname = request.POST['signupfname']
       signupsname = request.POST['signupsname']
       pass1 = request.POST['inputPassword1']
       pass2 = request.POST['inputPassword2']
       if len(user) > 10:
            messages.error(request,"user name should be less than 10 characters")
            return redirect('/')
       if pass1 != pass2:
            messages.error(request,"passwoard should be match")
            return redirect('/')

       if not user.isalnum():
           messages.error(request,"username must be in alphabhates and numaric")
           return redirect('/')
         
        


       myuser = User.objects.create_user(user,email,pass1)
       
       myuser.first_name= signupfname
       myuser.last_name = signupsname
       myuser.save()
       messages.success(request,"your account has been successfully created")
       return redirect('home')
    else:
        return render(request,'error.html')

def handlelogout(request):
    logout(request)
    messages.success(request,'successfully logout')
    return redirect('home')


def handlelogin(request):



    if request.method == 'POST':
       loginuser = request.POST['loginuser'] 
       loginPassword= request.POST['loginPassword']
       user = authenticate(username=loginuser,password=loginPassword)
       if user is not None:
            login(request,user)
            messages.success(request,"sucessfully login")
            return redirect('home')
       else:
           messages.error(request,'invalid username')
           return redirect('home')
    else:
        return render(request,'error.html')
    return render(request,'home.html')  