from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Emply,Leave
from .forms import EmplyForm
# Create your views here.

def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def add(request):
    if request.method=='POST':
        name=request.POST.get('names')
        designation=request.POST.get('designation')
        empid=request.POST.get('empid')
        dob=request.POST.get('dob')
        doj=request.POST.get('doj')
        department=request.POST.get('department')
        salary=request.POST.get('salary')
        email=request.POST.get ('email')
        # isAdmin=request.POST.get('isAdmin')
        obj=Emply(name=name,designation=designation,empId=empid,dob=dob,dateOfJ=doj,department=department,email=email,salary=salary)
        obj.save()

    return render(request,'add.html')

@login_required(login_url='login')
def table(request):
    task=Emply.objects.all()
    return render(request,'table.html',{'task':task})


def update(request,update_id):
    tasks=Emply.objects.get(id=update_id)
    form=EmplyForm(request.POST or None,instance=tasks)
    if form.is_valid():
        form.save()
        return redirect("http://127.0.0.1:8000/table")

    return render(request,'update.html',{'form':form})


def delete(request,delete_id):
    tasks=Emply.objects.get(id=delete_id)
    tasks.delete()
    return redirect("http://127.0.0.1:8000/table")

# def name_search(request):
#     name = request.GET.get('name', '')
#     if not name:
#         task=Emply.objects.all()
#     else:    
#         task = Emply.objects.filter(name__icontains=name)
#     return render(request,'table.html',{'task':task,'name':name})

# def department_search(request):
#     department = request.GET.get('department', '')
#     if not department:
#         task=Emply.objects.all()
#     else:    
#         task = Emply.objects.filter(department__icontains=department)
#     return render(request,'table.html',{'task':task,'department':department})

@login_required(login_url='login')
def applyleave(request):
    if request.method=='POST':
        fromDate=request.POST.get('fromDate')
        toDate=request.POST.get('toDate')
        typeOfleave=request.POST.get('typeOfleave')
        remarks=request.POST.get('remarks')
        current_user=str(request.user)
        obj1=Leave(fromDate=fromDate,toDate=toDate,typeOfLeave=typeOfleave,remarks=remarks,user=current_user,leaveStatus='Pending')
        obj1.save()

    return render(request,'applyleave.html')

@login_required(login_url='login')
def manageleave(request):
    leaves=Leave.objects.all()
    return render(request,'manageleave.html',{'leaves':leaves})

def approveleave(request,approve_id):
    leaves=Leave.objects.get(id=approve_id)
    leaves.leaveStatus='Approved'
    leaves.save()
    return redirect('manageleave')

def rejectleave(request,reject_id):
    leaves=Leave.objects.get(id=reject_id)
    leaves.leaveStatus='Rejected'
    leaves.save()
    return redirect('manageleave')

