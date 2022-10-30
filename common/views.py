from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
from .utils import  password_verify

from .forms import LoginForm

# Create your views here.
def login(request):
    #check if already logged
    if request.session.get('logged',False):
        return render(request,'index.html',{'user':request.session['user_name']})
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            _user=User.objects.filter(user_username=form.cleaned_data['user'])
            if _user:
                if password_verify(form.cleaned_data['password'],_user[0].user_password):
                    request.session['logged']=True
                    request.session['user_name']=form.cleaned_data['user']
                    return render(request, 'index.html',form.cleaned_data)
            #user/password error
            return render(request,'login.html',{'form':LoginForm(auto_id=False),
                                                'message':"User/Password Error"})
    else:
        return render(request,'login.html',{'form':LoginForm(auto_id=False),
                                            'message':'Sign in to start your session'})

def index(request):
    return login(request)
def logout(request):
    if request.session.get('logged',False):request.session.clear()
    return HttpResponseRedirect('/')