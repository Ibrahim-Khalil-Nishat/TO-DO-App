from django.shortcuts import render,redirect
from .models import Employee,Register,Group
from . import models
from .forms import EmployeeForm,RegisterForm,GroupForm


# Create your views here.
def welcome(request):
    return render(request,"welcome.html")


def load_form(request):
    form=EmployeeForm
    return render(request,'index.html',{'form':form})


def add(request):
    form=EmployeeForm(request.POST)
    form.save()
    return redirect('show')


def show(request):
    employee=Employee.objects.all
    return render(request,'show.html',{'employee':employee})


def edit(request, id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})


def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    form.save()
    return redirect('/show')

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('show')


def search(request):
        given_name=request.POST['name']
        employee=Employee.objects.filter(ename__contains=given_name)
        return render(request,'show.html',{'employee':employee})




def register(request):
    form=RegisterForm
    return render(request,'register.html',{'form':form})
def addd(request):
    form=RegisterForm(request.POST)
    form.save()
    return redirect('/watch')

def watch(request):
    register=Register.objects.all
    return render(request,'watch.html',{'register':register})

def editt(request, id):
    register=Register.objects.get(id=id)
    return render (request,'editt.html',{'register':register})


#Blood
def Gro(request):
    return render(request,'group.html')

def details(request):
    form=GroupForm
    return render(request,'details.html',{'form':form})

def Adddd(request):
    form=GroupForm(request.POST)
    form.save()
    return redirect('/regi')

def regi(request):
    group=Group.objects.all
    return render(request,'registerr.html',{'group':group})

def Dele(request,id):
    group=Group.objects.get(id=id)
    group.delete()
    return redirect('/regi')

def sea(request):
        given_name=request.POST['group']
        group=Group.objects.filter(group__iexact=given_name)
        return render(request,'registerr.html',{'group':group})



