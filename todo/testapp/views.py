from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def homeview(request):
    
    taskview=task.objects.all()
    formview=taskform()
    my_dict={"taskview":taskview,"formview":formview}
    if request.method=="POST":
        formview=taskform(request.POST)
        if formview.is_valid():
            formview.save(commit=True)
            
        return redirect('/')
    return render(request,"testapp/home.html",context=my_dict) 

def deletepost(request,pk):
    post=task.objects.get(pk=pk)
    post.delete()
    return redirect("/")

    
def updatetask(request,pk):
    taskupdate=task.objects.get(id=pk)
    print(taskupdate)
    return render(request,'testapp/update.html')
