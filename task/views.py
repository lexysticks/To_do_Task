from django.shortcuts import render,get_object_or_404,redirect
from . models import Task
from django.contrib import messages
from . forms import TaskForm,AddTaskForm
# Create your views here.
def home(request):
    tasks = Task.objects.all
    
    contexts ={
        'tasks':tasks
    }
    return render(request,'task/home.html',contexts)

def TaskEdit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('home')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm(instance=task)

    contexts = {
        'task': task,
        'form': form,
    }
    return render(request, 'task/edit_task.html', contexts)

def add_task(request):
    if request.method =='POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'task added successfully')
            return redirect('home')
        else:
            messages.error(request,'invalid task')
    else:
        form =AddTaskForm()
    contextss ={
        'form':form
    }
    return render(request,'task/add_task.html',contextss)
    
    
def delete(request,pk):
    task= get_object_or_404(Task,pk=pk)
    if request.method =='POST':
        task.delete()
        messages.success(request,'Task Deleted Successfully')
        return redirect('home')
    return render(request,'task/delete.html')

    