from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task

from django.urls import reverse_lazy


# Create your views here.
class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetailView(DetailView):
    template_name = "base/task.html"
    model = Task
    context_object_name = "task"

# CreateView e UpdateView por padrão olham para <moduleName>_form.html
class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDeleteView(DeleteView):
    template_name = "base/task_delete.html"
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = "task"