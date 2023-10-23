from django.urls import path
from . import views

urlpatterns = [
    path('', views.takList, name='task')
]