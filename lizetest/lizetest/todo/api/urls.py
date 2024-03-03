from django.urls import path
from .views import  TaskViewUpdateStatus


app_name = "api_tasks"

urlpatterns = [
    path('tasks/<int:pk>/', TaskViewUpdateStatus.as_view(), name='task_list'),
]

