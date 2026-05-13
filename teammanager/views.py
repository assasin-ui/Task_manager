from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from rest_framework.decorators import api_view

from rest_framework.response import Response

from tasks.serializers import TaskSerializer

from projects.serializers import ProjectSerializer
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from users.models import User
from users.models import User

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/')

    return render(request, 'login.html')


def logout_view(request):

    logout(request)

    return redirect('/login/')

def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    total_projects = Project.objects.count()

    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(
        status='completed'
    ).count()

    pending_tasks = Task.objects.filter(
        status='pending'
    ).count()

    in_progress_tasks = Task.objects.filter(
        status='in_progress'
    ).count()

    recent_tasks = Task.objects.order_by(
        '-id'
    )[:5]

    context = {
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'recent_tasks': recent_tasks,
    }

    return render(request, 'dashboard.html', context)


def project_list(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'projects.html', context)

def task_list(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.user.role == 'admin':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(
            assigned_to=request.user
        )

    search_query = request.GET.get('search')

    status_filter = request.GET.get('status')

    if search_query:
        tasks = tasks.filter(
            title__icontains=search_query
        )

    if status_filter:
        tasks = tasks.filter(
            status=status_filter
        )

    context = {
        'tasks': tasks
    }

    return render(request, 'tasks.html', context)

def create_task(request):

    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.user.role != 'admin':
        return redirect('/')

    projects = Project.objects.all()

    users = User.objects.all()

    if request.method == 'POST':

        title = request.POST.get('title')

        description = request.POST.get('description')

        due_date = request.POST.get('due_date')

        project_id = request.POST.get('project')

        assigned_user_id = request.POST.get('assigned_to')

        project = Project.objects.get(id=project_id)

        assigned_user = User.objects.get(id=assigned_user_id)

        Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status='pending',
            assigned_to=assigned_user,
            project=project
        )
        messages.success(
                request,
                    'Task created successfully'
        )
        return redirect('/tasks/')

    context = {
        'projects': projects,
        'users': users
    }

    return render(request, 'create_task.html', context)
def logout_view(request):
    logout(request)
    return redirect('/login/')
def update_task_status(request, task_id):

    if not request.user.is_authenticated:
        return redirect('/login/')

    task = Task.objects.get(id=task_id)
    if (
        request.user.role != 'admin'
        and task.assigned_to != request.user
    ):
        return redirect('/tasks/')
    if request.method == 'POST':

        new_status = request.POST.get('status')

        task.status = new_status

        task.save()
        messages.success(
        request,
        'Task status updated'
)

    return redirect('/tasks/')
def create_project(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.user.role != 'admin':
        return redirect('/')

    users = User.objects.all()

    if request.method == 'POST':

        title = request.POST.get('title')

        description = request.POST.get('description')

        team_member_ids = request.POST.getlist(
            'team_members'
        )

        project = Project.objects.create(
            title=title,
            description=description,
            created_by=request.user
        )

        project.team_members.set(team_member_ids)
        messages.success(
        request,
        'Project created successfully'
        )
        return redirect('/projects/')

    context = {
        'users': users
    }

    return render(
        request,
        'create_project.html',
        context
    )
def delete_task(request, task_id):

    if not request.user.is_authenticated:
        return redirect('/login/')

    task = Task.objects.get(id=task_id)

    if request.user.role != 'admin':
        return redirect('/tasks/')

    task.delete()
    messages.success(
        request,
        'Task deleted successfully'
    )
    return redirect('/tasks/')
def edit_task(request, task_id):

    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.user.role != 'admin':
        return redirect('/tasks/')

    task = Task.objects.get(id=task_id)

    if request.method == 'POST':

        task.title = request.POST.get('title')

        task.description = request.POST.get(
            'description'
        )

        task.due_date = request.POST.get(
            'due_date'
        )

        task.save()

        return redirect('/tasks/')

    context = {
        'task': task
    }

    return render(
        request,
        'edit_task.html',
        context
    )
def edit_project(request, project_id):

    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.user.role != 'admin':
        return redirect('/projects/')

    project = Project.objects.get(id=project_id)

    if request.method == 'POST':

        project.title = request.POST.get('title')

        project.description = request.POST.get(
            'description'
        )

        project.save()
        messages.success(
        request,
        'Project updated successfully'
        )
        return redirect('/projects/')

    context = {
        'project': project
    }

    return render(
        request,
        'edit_project.html',
        context
    )
def delete_project(request, project_id):

    if not request.user.is_authenticated:
        return redirect('/login/')

    if request.user.role != 'admin':
        return redirect('/projects/')

    project = Project.objects.get(id=project_id)

    project.delete()
    messages.success(
        request,
        'Project deleted successfully'
    )       
    return redirect('/projects/')
@api_view(['GET'])
def task_api(request):

    tasks = Task.objects.all()

    serializer = TaskSerializer(
        tasks,
        many=True
    )

    return Response(serializer.data)


@api_view(['GET'])
def project_api(request):

    projects = Project.objects.all()

    serializer = ProjectSerializer(
        projects,
        many=True
    )

    return Response(serializer.data)
def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists'
            )

            return redirect('/signup/')

        user = User.objects.create(
            username=username,
            email=email,
            role='member'
        )

        user.set_password(password)

        user.save()

        messages.success(
            request,
            'Account created successfully'
        )

        return redirect('/login/')

    return render(request, 'signup.html')