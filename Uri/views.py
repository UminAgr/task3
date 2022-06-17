from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks=Task.objects.all()
    return render(request,'Uri/index.html', {'title':'Главная страница сайта', 'tasks':tasks})

def about(request):
    return render(request,'Uri/about.html',{'title':'Твоя страница'})

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        "form": form,
        "error" : error
    }
    return render(request,'Uri/create.html',{'title':'Нужная страница'} , context)