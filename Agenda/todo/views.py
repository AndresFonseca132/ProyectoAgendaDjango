from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.
def index(request):
    todos = Todo.objects.filter(title__icontains=request.GET.get('search', ''))
    return render(request, 'todo/index.html', {'todos': todos})


def view(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/detail.html', context)

def edit(request, id):
    todo = Todo.objects.get(id=id)

    if(request.method == 'GET'):
        form = TodoForm(instance=todo)
        context = {
            'form': form,
            'id':id
        }
        return render(request, 'todo/edit.html', context)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea actualizado.')
            return redirect('todo')


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha creado la tarea')
            return redirect('todo')  # Redirige a la lista de contactos o a otra URL de tu elección
    else:
        form = TodoForm()
    
    context = {
        'form': form
    }
    return render(request, 'todo/create.html', context)


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    messages.success(request, 'Tarea eliminada.')
    return redirect('todo')