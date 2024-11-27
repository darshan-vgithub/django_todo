from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Todo.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'todo/todo_add.html')

def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo/todo_edit.html', {'todo': todo})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_delete.html', {'todo': todo})
