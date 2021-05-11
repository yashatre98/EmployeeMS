from django.shortcuts import render
from ems.models import Employee
from django.contrib import messages
from .forms import EMform

def empdisplay(request):
    res=Employee.objects.all()
    return render(request, 'index.html',{'Employee':res})


def EMinsert(request):
    if(request.method=="POST"):
        if(request.POST.get('name') and request.POST.get('email') and request.POST.get('mob') and request.POST.get('gender')):
            save_em=Employee()
            save_em.name=request.POST.get('name')
            save_em.email=request.POST.get('email')
            save_em.mob=request.POST.get('mob')
            save_em.gender=request.POST.get('gender')
            save_em.save()
            messages.success(request, "the record for "+save_em.name+" is saved successfully.")
            return render(request,'create.html')
    else:
        return render(request, 'create.html')


def EMedit(request,id):
    getEM=Employee.objects.get(id=id)
    return render(request, 'edit.html',{'Employee':getEM})


def EMupdate(request,id):
    emupdate=Employee.objects.get(id=id)
    print("##### "+emupdate.name)
    form=EMform(request.POST,instance=emupdate)
    if(form.is_valid()):
        form.save()
        messages.success(request,"Updated successfully")
        print("*****"+emupdate.name)
        return render(request, 'edit.html',{'Employee':emupdate}) 
    return render(request, 'edit.html',{})

def EMdelete(request,id):
    emdel=Employee.objects.get(id=id)
    emdel.delete()
    res=Employee.objects.all()
    return render(request, 'index.html',{'Employee':res})
