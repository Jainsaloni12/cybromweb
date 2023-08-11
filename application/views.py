from django.shortcuts import render
from .models import ServiceCybrom,ProjectCybrom,AboutCybrom,Contact_us,ServiceRelated,SectionSix
from .forms import ShowImage
from .forms import SignUpForm
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

global lis
lis=[]

def home(req):
    return render(req,"application/index.html")

def sign_up(req):
    if req.method=="POST":
        fm=SignUpForm(req.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=SignUpForm()
    return render(req,'application/signup.html',{'fm':fm})

def log_in(req):
    if req.method=='POST':
        fm=LoginForm(request=req,data=req.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            passw=fm.cleaned_data['password']
            user=authenticate(username=username,password=passw)
            if user is not None:
                login(req,user)
                user1=True
                return render(req,'application/index.html',{'current_user':req.user,'user1':user1})
    else:
        fm=LoginForm()
    return render(req,'application/login.html',{'fm':fm})
    
def log_out(req):
    logout(req)
    return HttpResponseRedirect('/login')




def index(req):
    global lis
    lis=[]
    print(str(req.user))
    if str(req.user)=='AnonymousUser':
        print('heree')
        user1=False
    else:
        user1=True
    data=ServiceCybrom.objects.all()
    project=ProjectCybrom.objects.all()

    return render(req,'application/index.html',{'current_user':req.user,'user1':user1,'data':data,
                                                'project':project})

def about(req):
    ab=AboutCybrom.objects.all()
    return render(req,'application/about.html',{'fm':ab})

def contact(req):
    if req.method=='POST':
        print(req.POST)
        name=req.POST.get('sn')
        email=req.POST.get('se')
        mobile=req.POST.get('sm')
        msg=req.POST.get('Message')
        instance=Contact_us(name=name,email=email,mobile_no=mobile,query=msg)
        instance.save()
        msg=True
    else:
        msg=False
    user1=False
    if str(req.user)=='AnonymousUser':
        user1=False
    else:
        user1=True
    return render(req,'application/contact.html',{'msg':msg,'current_user':req.user,'user1':user1})

def project(req):
    if req.method=='POST':
        form=ShowImage(req.POST,req.FILES)
        if form.is_valid():
            form.save()
    form=ShowImage()
    client_data=SectionSix.objects.all()
    project=ProjectCybrom.objects.all()
    return render(req,'application/project.html',{'form':form,'project':project,'data':client_data})

def service(req):
    data=ServiceCybrom.objects.all()
    return render(req,'application/service.html',{'data':data})


def desc(req,id):
    data=ServiceCybrom.objects.get(pk=id)
    id1=ServiceRelated.objects.values().filter(name=data)[0].get('id')
    data2=ServiceRelated.objects.get(pk=id1)
    print(data2)
    return render(req,'application/desc.html',{'i':data,'i2':data2})


def enroll(req):
    global lis
    lis=lis
    data=ServiceCybrom.objects.all()

    return render(req,'application/enroll.html',{'data':data,'course':lis})

def enrollmore(req):
    global lis
    lis=lis
    data=ServiceCybrom.objects.all()
    if req.method=="POST":
         course=req.POST.get('ch')
         if course not in lis:
            lis.append(course)
         else:
            msg="u already selected"
            return render(req,'application/enroll.html',{'data':data,'course':lis,'msg':msg})
         
    data=ServiceCybrom.objects.all()

    return render(req,'application/enroll.html',{'data':data,'course':lis})

# course =req.POST.get('ch) python

def final(req):
    total=0
    global lis
    lis=lis
    lis2=[]
    print(lis)
    for i in lis:
        print (i)
        # data=ServiceCybrom.objects.get(name=i)
        # print(data)
        id1=ServiceRelated.objects.values().filter(name=i)
        fees=id1[0].get('fees')
        li1=[i,fees]
        lis2.append(li1)
        total=total+fees


    print(total)
    return render(req,'application/final.html',{'lis2':lis2,'total':total})
    
def remove(req,sub):
    global lis
    lis=lis
    lis.remove(sub)
    return HttpResponseRedirect('/enroll')  


