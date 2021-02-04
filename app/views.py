from django.shortcuts import render,redirect
from django.views.generic import View , TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login,logout , authenticate
from .models import *
from .forms import *
import  random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q

# Create your views here.

class Home(LoginRequiredMixin,View):
    def get(self,request):
        context = {"blog":Blogs.objects.filter(user=request.user)}
        return render(request, 'private/home.html', context)

class Singup(View):
    def get(self,request):
        form  = SignupForm()
        #data = random.choice(Captcha.objects.all())
        no1 = random.randint(1,20)
        operator = random.choice(['+','-'])
        no2 = random.randint(0,30)

        context = {
            "form": form,
            "no1":no1,
            "operator":operator,
            "no2":no2,

        }
        return render(request,'public/signup.html',context)

    def post(self,request):
        form = SignupForm(request.POST or None)

        no1 = request.POST.get('no1')
        no2 = request.POST.get('no2')
        opr = request.POST.get('opr')
        ans = request.POST.get('captcha')
        username = request.POST.get('username')

        check = eval(str(no1)+opr+str(no2))

        #check username langth
        if not (len(username)) >= 10:
            messages.error(self.request ,"Username not 10 character please choice username minimum 10 chaaracter ")
            return redirect('singup')

        #check Captcha
        if (int(check) == int(ans)):
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                messages.error(self.request,"password does not match")
                return redirect('singup')
        else:
            messages.error(self.request ,"Value not match please Enter the currect value")
            return redirect('singup')


class Login(View):
    def get(self,request):
        return render(request,'public/login.html')
    def post(self,request):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'public/login.html')


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')



class AddNewArticle(LoginRequiredMixin,View):
    def get(self,request):
        form = AddBlogForm()
        return render(request,'private/addblog.html',{"forms":form})

    def post(self,request):
        form = AddBlogForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            a = form.save(commit=False)
            a.user = request.user
            a.save()
            return redirect('home')


class SearchBlog(LoginRequiredMixin,View):
    def get(self,request):
        search = request.GET.get('search')
        cond = Q(user__username=search ,status='PUBLIC') | Q(title__icontains = search,status = 'PUBLIC')
        context = {"blog":Blogs.objects.filter(cond)}
        return render(request,'private/home.html',context)






