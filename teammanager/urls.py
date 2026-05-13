from django.contrib import admin
from django.urls import path, include
from .views import logout_view
from .views import (
    login_view,
    signup_view,
    logout_view,
    dashboard,
    project_list,
    task_list,
    create_task,
    update_task_status,
    create_project,
    delete_task,
    edit_task,
    edit_project,
    delete_project,
    task_api,
    project_api,
    
)


urlpatterns = [

    path('admin/', admin.site.urls),

    path('login/', login_view),
    path('signup/', signup_view),

    path('logout/', logout_view),

    path('', dashboard),

    path('projects/', project_list),
    path(
        'projects/edit/<int:project_id>/',
        edit_project
    ),
    path(
        'projects/delete/<int:project_id>/',
         delete_project
    ),
    path(
        'projects/create/',
        create_project
    ),

    path('tasks/', task_list),
    path(
        'tasks/edit/<int:task_id>/',
        edit_task
    ),
    path(
        'tasks/delete/<int:task_id>/',
        delete_task
    ),
    path(
        'tasks/update/<int:task_id>/',
        update_task_status
        ),
    path('tasks/create/', create_task),

    path('api/', include('projects.urls')),
    path('api/', include('tasks.urls')),
    path('api/tasks/', task_api),

    path('api/projects/', project_api),
]