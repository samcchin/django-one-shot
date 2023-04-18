from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm


# Create your views here.
def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_list_list": todo_lists,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    todo_list = TodoList.objects.get(id=id)
    context = {
        "todo_list_detail": todo_list,
    }
    return render(request, "todos/detail.html", context)


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            list = form.save(False)
            list.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm()
    context = {
        "form": form
    }
    return render(request, "todos/create.html", context)
