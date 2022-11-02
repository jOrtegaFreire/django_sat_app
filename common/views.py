from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Ingress, User,Component,Client,Appliance
from .utils import  password_hash,password_verify,ingress_status

from .forms import LoginForm,AddComponentForm,EditComponentFormHelper,EditComponentForm
from .forms import UserRegisterForm,CheckClientForm,NewClientForm,NewIngressForm

from datetime import datetime

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

def register(request):
    if request.session.get('logged',False):
        return render(request,'index.html',{'user':request.session['user_name']})
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            # check if username exist
            u=User.objects.filter(user_username=form.cleaned_data['user_username'])
            if len(u)!=0:
                #username exist in database
                return register_error(request,'The username is not available')
            # check if email is already registered              
            u=User.objects.filter(user_email=form.cleaned_data['user_email'])
            if len(u)!=0:
                #email already registered
                return register_error(request,'The email is already in use')
            #check passwords match
            if form.cleaned_data['user_password1']!=form.cleaned_data['user_password2']:
                #password mismatch
                return register_error(request,'Password mismatch')
            #create new user
            u=User(user_username=form.cleaned_data['user_username'],
                   user_type='pending',
                   user_first_name=form.cleaned_data['user_first_name'],
                   user_last_name=form.cleaned_data['user_last_name'],
                   user_email=form.cleaned_data['user_email'],
                   user_password=password_hash(form.cleaned_data['user_password1']))
            u.save()
            return render(request,'register_result.html',{'message':'Resgister completed'}) 
        return render(request,'register.html',{'form':UserRegisterForm(auto_id=False),
                                               'message':'Register a new membership'})
    else:
        return render(request,'register.html',{'form':UserRegisterForm(auto_id=False),
                                               'message':'Register a new membership'})

def register_error(request,message):
    return render(request,'register.html',{'form':UserRegisterForm(auto_id=False),
                                            'message':message})

def index(request):
    return login(request)
def logout(request):
    if request.session.get('logged',False):request.session.clear()
    return HttpResponseRedirect('/')

def add_component(request):
    if request.session.get('logged',False):
        success=False
        if request.method=='POST':
            form=AddComponentForm(request.POST)
            if form.is_valid():
                #insert values to db
                c=Component(component_code=form.cleaned_data['component_code'],
                            component_qty=form.cleaned_data['component_qty'],
                            component_price=form.cleaned_data['component_price'],
                            component_description=form.cleaned_data['component_description'])
                c.save()
                success=True
                components=Component.objects.all()
                return render(request,'stock.html',{'user':request.session['user_name'],
                                                    'components':components,
                                                    'success':success,
                                                    'message':'Component Added to the Database'})
        return render(request,'add_component.html',{'form':AddComponentForm(auto_id=False),
                                                    'user':request.session['user_name']})
    else: return login(request)

def stock(request,message=None):
    # check if session in logged in 
    if request.session.get('logged',False):
        # check if component was edited to the db
        if message is not None:
            components=Component.objects.all()
            return render(request,'stock.html',{'user':request.session['user_name'],
                                                'components':components,
                                                'success':True,
                                                'message':message})
        # check if we're editing a component
        if request.method=='POST':
            form=EditComponentFormHelper(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                component=Component.objects.filter(component_code=form.cleaned_data['component_code'])[0]
                data={ 'component_code':component.component_code,
                       'component_qty':component.component_qty,
                       'component_price':component.component_price,
                       'component_description':component.component_description}
                #edit component information
                return edit_component(request,{'user':request.session['user_name'],
                                                'form':EditComponentForm(data)})
        #if not render the stock page
        components=Component.objects.all()
        return render(request,'stock.html',{'user':request.session['user_name'],
                                            'components':components})
    # if not, redirect to login page
    else: return login(request)

def edit_component(request,context=None):
    if request.session.get('logged',False):
        if request.method=='POST':
            form=EditComponentForm(request.POST)
            if form.is_valid():
                if 'delete' in list(request.POST):
                    c=Component.objects.filter(component_code=form.cleaned_data['component_code'])[0]
                    c.delete()
                    return stock(request,"Component deleted successfully")
                c=Component.objects.filter(component_code=form.cleaned_data['component_code'])[0]
                c.component_qty=form.cleaned_data['component_qty']
                c.component_price=form.cleaned_data['component_price']
                c.component_description=form.cleaned_data['component_description']
                c.save()
                components=Component.objects.all()
                return stock(request,"Component edited successfully")
        return render(request,'edit_component.html',context)
    return login(request)

def ingress(request,message=None):
    if request.session.get('logged',False):
        if request.method=='POST':
            if len(request.POST)==2:form=CheckClientForm(request.POST)
            elif len(request.POST)==7:form=NewClientForm(request.POST)
            else:form=NewIngressForm(request.POST)
            if form.is_valid():
                print(len(request.POST))
                if len(request.POST)==2:
                    # check if client is registered
                    client=Client.objects.filter(client_id=form.cleaned_data['client_id'])
                    if len(client)!=0:
                        # render ingress form with autofill client info
                        return new_ingress(request,{'user':request.session['user_name'],
                                                    'client_id':form.cleaned_data['client_id']})
                    else:
                        #render new client page
                        return new_client(request,{'user':request.session['user_name'],
                                                'client_id':form.cleaned_data['client_id']})
                elif len(request.POST)==7:
                    # add client and continue to ingress
                    client=Client(client_id=form.cleaned_data['client_id'],
                                  first_name=form.cleaned_data['first_name'],
                                  last_name=form.cleaned_data['last_name'],
                                  email=form.cleaned_data['email'],
                                  phone_number=form.cleaned_data['phone_number'])
                    client.save()
                    return new_ingress(request,{'user':request.session['user_name'],
                                                'client_id':form.cleaned_data['client_id']})
                else:
                    # save Appliance info
                    appliance=Appliance(appliance_type=form.cleaned_data['appliance_type'],
                                        appliance_brand=form.cleaned_data['appliance_brand'],
                                        appliance_model=form.cleaned_data['appliance_model'],
                                        appliance_sn=form.cleaned_data['appliance_sn'])
                    appliance.save()
                    # get client object
                    client=Client.objects.filter(client_id=form.cleaned_data['client_id'])[0]
                    # save ingress data
                    ingress=Ingress(ingress_date=datetime.strptime(form.cleaned_data['ingress_date'],"%d/%m/%y"),
                                    client=client,
                                    appliance=appliance,
                                    failure_description=form.cleaned_data['failure_description'],
                                    inspection_status=form.cleaned_data['inspection_status'],
                                    accessories=form.cleaned_data['accessories'],
                                    state=0,
                                    quotation=0)
                    ingress.save()

        return render(request,'check_client_id.html',{'user':request.session['user_name'],
                                                      'form':CheckClientForm(auto_id=False)})
    else: return login(request)

def new_client(request,context):
    form=NewClientForm({'client_id':context['client_id']})
    context['form']=form
    return render(request,'new_client.html',context)

def new_ingress(request,context):
    client=Client.objects.filter(client_id=context['client_id'])[0]
    form=NewIngressForm({'client_id':client.client_id,
                         'first_name':client.first_name,
                         'last_name':client.last_name,
                         'email':client.email,
                         'phone_number':client.phone_number})
    return render(request,'new_ingress.html',{'user':request.session['user_name'],
                                              'form':form})

def show_all(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get all entries
            entries=Ingress.objects.all()
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'All Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def show_received(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get received entries
            entries=Ingress.objects.filter(state=0)
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'Received Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def show_inspecting(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get received entries
            entries=Ingress.objects.filter(state=1)
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'Received Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def show_awaiting_approval(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get received entries
            entries=Ingress.objects.filter(state=2)
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'Received Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def show_repairing(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get received entries
            entries=Ingress.objects.filter(state=3)
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'Received Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def show_repaired(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get received entries
            entries=Ingress.objects.filter(state=4)
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'Received Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def show_delivered(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get received entries
            entries=Ingress.objects.filter(state=5)
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'Received Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def show_pending_return(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get received entries
            entries=Ingress.objects.filter(state=6)
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'Received Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def show_returned(request):
    if request.session.get('logged',False):
        if request.method=='POST':pass
        else:
            # get received entries
            entries=Ingress.objects.filter(state=7)
            return render(request,'ingress_all.html',{'user':request.session['user_name'],
                                                      'title':'Received Appliances',
                                                      'entries':get_ingress_data(entries)})
    else: return login(request)

def get_ingress_data(entries):
    _entries=[]
    for entry in entries:
        # get client info
        client=Client.objects.filter(client_id=entry.client_id)[0]
        client_info='['+client.client_id+'] '+client.first_name+' '+client.last_name
        # get appliance info
        appliance=Appliance.objects.filter(id=entry.appliance_id)[0]
        appliance_info=appliance.appliance_type+' '+appliance.appliance_brand+' Mod. '+appliance.appliance_model
        ingress_status_info=ingress_status(entry.state)
        _entry=dict()
        _entry['ingress_id']=entry.id
        _entry['client']=client_info
        _entry['appliance']=appliance_info
        _entry['status']=ingress_status_info
        _entries.append(_entry)
    return _entries

def ingress_edit(request,message=None):
    pass