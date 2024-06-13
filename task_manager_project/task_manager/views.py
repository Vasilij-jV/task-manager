from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Task
from django.http import HttpResponse


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'task/list_task.html', {'tasks': tasks})




