from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
# Create your views here.
def home(request):
    tasks = Task.objects.all()
    forms = TaskForm()

    if request.method == 'POST':
        forms =TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    context = {'tasks':tasks,'forms':forms}
    return render(request,'myapp/home.html',context)


def updateTask(request,pk):
    tasks = Task.objects.get(id=pk)
    forms = TaskForm(instance=tasks)
    if request.method == 'POST':
        forms = TaskForm(request.POST,instance=tasks)
        if forms.is_valid():
            forms.save()
            return redirect('home')

    context = {'tasks':tasks,'forms':forms}
    return render(request,'myapp/updatetask.html',context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
 
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    
    context = {'item':item}

    return render(request,'myapp/delete.html',context)