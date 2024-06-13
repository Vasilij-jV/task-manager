from django.urls import path
from . import views

app_name = 'task_manager'

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
   ]
