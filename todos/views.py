from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


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
    context = {"form": form}
    return render(request, "todos/create.html", context)


def todo_list_update(request, id):
    todo_lists = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_lists)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=todo_lists)

    context = {
        "todo_lists": todo_lists,
        "form": form,
    }

    return render(request, "todos/edit.html", context)


def todo_list_delete(request, id):
    todo_lists = TodoList.objects.get(id=id)
    if request.method == "POST":
        todo_lists.delete()
        return redirect("todo_list_list")
    return render(request, "todos/delete.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            item = form.save(False)
            item.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm()
    context = {"form": form}
    return render(request, "todos/items_create.html", context)


def todo_item_update(request, id):
    todo_item = TodoItem.objects.get(id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todo_item)
        if form.is_valid():
            item = form.save()
            return redirect("todo_list_detail", id=item.list.id)
    else:
        form = TodoItemForm(instance=todo_item)
    context = {
        "todo_item": todo_item,
        "form": form,
    }
    return render(request, "todos/items_edit.html", context)
