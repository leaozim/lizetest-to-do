from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, CategoryListView, CategoryDatailView

app_name = "todo"

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDatailView.as_view()),


]
 # CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

    # path('category', CategoryListView.as_view(), name='category_list'),
    # path('category/create', CategoryCreateView.as_view(), name='category_create'),
    # path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    # path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),