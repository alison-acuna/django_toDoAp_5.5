from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ToDo
from .forms import PostForm
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
    form = PostForm()
    return render(request, 'todo/new.html', {
        'form': form
    })
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user
    #         post.date_created = timezone.now()
    #         post.save()
    #         return redirect('post_detail', pk=post.pk)
    # else:
    #     form = PostForm()
    # return render(request, 'todo_new.html', {
    #     'form': form
    #     })


def add_new(request):
    onClick(".save_btn_btn-default")
    item = ToDo.objects.get(pk=id)
