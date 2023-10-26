from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, CustoomLoginViw, RegisterUserFormView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustoomLoginViw.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', RegisterUserFormView.as_view(), name='registro'),
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task'),
    path('task-create/', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]