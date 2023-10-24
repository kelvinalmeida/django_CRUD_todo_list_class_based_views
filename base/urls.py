from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
]