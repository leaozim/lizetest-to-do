
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('todo:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')
    
    
# from rest_framework import generics, permissions
# from .models import Category
# from .serializers import CategorySerializer


# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
    
# class CategoryCreateView(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryUpdateView(generics.UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]  


# class CategoryDeleteView(generics.DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class CategoryListView(APIView):
    
    def get (self, request, format=None):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post (self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDatailView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
        
    def get (self, request, pk, formatt=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put (self, request, pk, formatt=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.error)
    
    def delete (self, request, pk, formatt=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
