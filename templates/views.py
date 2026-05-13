from django.shortcuts import render

from projects.models import Project
from tasks.models import Task


def dashboard(request):

    total_projects = Project.objects.count()

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(
        status='completed'
    ).count()

    context = {
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'dashboard.html', context)