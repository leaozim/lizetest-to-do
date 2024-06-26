
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import UpdateAPIView
from ..models import Task

from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated  



class TaskViewUpdateStatus(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    fields = ['completed'] 
    permission_classes = [IsAuthenticated]
    

    

        
        
        

