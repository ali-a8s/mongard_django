from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoCreateUpdateForm
from django.contrib import messages


# Create your views here.
def HomeView(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})


def DetailView(request, todo_id):
    todo = Todo.objects.get(pk= todo_id)
    return render(request, 'detail.html', {'todo': todo})


def DeleteView(request, todo_id):
    Todo.objects.get(pk= todo_id).delete()
    messages.success(request, 'todo deleted succussfully', 'success')
    return redirect('home')


def CreateView(request):
    if request.method == 'POST':
        form = TodoCreateUpdateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title= cd['title'], body= cd['body'])
            messages.success(request, 'todo created succussfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateUpdateForm()
    return render(request, 'create.html', {'form': form})
    

def UpdateView(request, todo_id):
    todo = Todo.objects.get(pk= todo_id)
    if request.method == 'POST':
        form = TodoCreateUpdateForm(request.POST, instance= todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'todo updated succussfully', 'success')
            return redirect('home')
    else:
        form = TodoCreateUpdateForm(instance= todo)
    return render(request, 'update.html', {'form': form})
    