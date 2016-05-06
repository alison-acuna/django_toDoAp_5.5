from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ToDo
from .forms import PostForm, DeleteForm
from django.utils import timezone
# Create your views here.


@login_required

def todo_item(request, id):
    item = ToDo.objects.get(pk=id)
    # used to pass different items by field
    # pk is the primary key field
    return render(request, 'todo/item.html', {
        'item': item
    })

def todo_list(request):
    todo = ToDo.objects.all()
    # return all instances of a model and assign to a variable
    # pk is the primary key field
    return render(request, 'todo/list.html', {
        'todo': todo
        # Assigns a todos variable to todos dictionary which inserts all to do
        # items to todo template.
    })

# def todo_add(request):
#
def todo_new(request):
    # form = PostForm()
    # return render(request, 'todo/new.html', {
    #     'form': form
    # })
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date_created = timezone.now()
            post.save()
            return redirect('todo_item', id=post.pk)
    else:
        form = PostForm()
    return render(request, 'todo/new.html', {
        'form': form
    })

def todo_edit(request, id):
    post = get_object_or_404(ToDo, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date_created = timezone.now()
            post.save()
            return redirect('todo_item', id=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'todo/new.html', {
        'form': form
    })

def todo_delete (request, id):
    new_to_delete = get_object_or_404(ToDo, pk=id)
    if request.method == "POST":
        form = DeleteForm(request.POST, instance=new_to_delete)
        if form.is_valid():
            new_to_delete.delete()
            return redirect('todo_list')
    else:
        form = DeleteForm()
        return render(request, 'todo/delete.html', {
            'form': form
            })


# def todo_delete (request):
    # form = DeleteForm(instance=new_to_delete)
    # return render(request, 'todo/delete.html', {
    #     'form': form
    #     })
