# forms.py

from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category']
        
    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', None)
        super(TaskForm, self).__init__(*args, **kwargs)

        if author:
            self.fields['category'].queryset = Category.objects.filter(author=author)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']