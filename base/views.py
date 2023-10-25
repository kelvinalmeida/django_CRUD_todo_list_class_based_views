from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

# Create your views here.

class CustoomLoginViw(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('tasks')

    
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = "base/task.html"
    model = Task
    context_object_name = "task"

# CreateView e UpdateView por padrão olham para <moduleName>_form.html
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "base/task_delete.html"
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = "task"