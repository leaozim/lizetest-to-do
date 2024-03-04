
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseForbidden

from .models import Task, Category
from .forms import TaskForm, CategoryForm



class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
    
    
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        if task.completed:
            return HttpResponseForbidden("Você não tem permissão.")
        return super().delete(request, *args, **kwargs)
            
            
            
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'category_list.html'
    success_url = reverse_lazy('todo:category_list')
    
    def get_queryset(self):
        return Category.objects.filter(author=self.request.user)
    
    
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('todo:category_list')
    
    def form_valid(self, form):
        if Category.objects.filter(name=form.instance.name).exists():
            form.add_error('name', 'This category name already exists.')
            return self.form_invalid(form)
        
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('todo:category_list')
    

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('todo:category_list')
    

