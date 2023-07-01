from django.shortcuts import render,redirect
from .forms import EmpForm
from .models import employe
# Create your views here.
def add(request):
    empForm=EmpForm()
    return render(request,'addemp.html',{'empForm':empForm})
def insertEmp(request):
    if request.method == "POST":
        empForm = EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return render(request,'signin.html',{'empForm':EmpForm(),'msg':"Employee Added..!!"})
        else:
            return render(request,'addemp.html')
    else:
        return render(request,'addemp.html')
def show(request):
    employees = employe.objects.all()
    return render(request,'show.html',{'employees':employees})

def editEmp(request,eid):
    emp = employe.objects.get(eid=eid)
    return render(request,'edit.html',{'emp':emp})

def updateEmp(rquest,eid):
    if rquest.method == "POST":
        emp = employe.objects.get(eid=eid)
        form = EmpForm(rquest.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('show.html')
        else:
            return render(request,'edit.html',{'emp':emp,'msg':'Details Not Updated...!!!'})
    else:
            return render(request,'edit.html',{'emp':emp,'msg':'Details Not Updated...!!!'})

