from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
def employe_list(request):
    context = {'employe_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

def employe_form(request,id=0):
    form = EmployeeForm()
    if request.method == "GET":
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"employee_register/employe_form.html",{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form= EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/Employee/list')

def employe_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/Employee/list')
