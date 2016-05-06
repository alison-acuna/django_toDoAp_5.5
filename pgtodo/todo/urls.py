from django.conf.urls import url
from . import views

urlpatterns = [
    # this specifies all of the routes in one place
    url(r'^todo/(?P<id>\d+)/$', views.todo_item, name='todo_item'),
    url(r'^todo/list', views.todo_list, name='todo_list'),
    url(r'^todo/new', views.todo_new, name='todo_new'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^todo/(?P<id>\d+)/edit/$', views.todo_edit, name='todo_edit'),
    url(r'^todo/(?P<id>\d+)/delete/$', views.todo_delete, name="todo_delete"),
]
