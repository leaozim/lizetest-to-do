from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from lizetest.accounts.models import User
from .models import Category, Task

class CategoryViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_category_list_view(self):
        category_1 = Category.objects.create(name='Test Category 1', author=self.user)
        category_2 = Category.objects.create(name='Test Category 2', author=self.user)
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('todo:category_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(set(response.context["categories"]), set([category_1, category_2]))
        self.assertTemplateUsed(response, 'category_list.html')
     
     
    def test_category_create_view(self):
        category_name = 'category1'
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todo:category_create'), {'name': category_name})
        
        latest_category_created = Category.objects.last()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(latest_category_created.name, category_name)
        self.assertEqual(latest_category_created.author, self.user)


    def test_duplicate_category_create_view_error(self):
        category_name = 'category2'
        Category.objects.create(name=category_name, author=self.user)
        copy_category_name = category_name
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todo:category_create'), {'name': copy_category_name})
        form = response.context["form"]
        
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This category name already exists.'])

    
    def test_category_create_view_with_invalid_data(self):
        category_name = None

        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todo:task_create'),category_name)
        form = response.context["form"]
        
        latest_task_created = Category.objects.last()

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], ['This field is required.'])
        self.assertIsNone(latest_task_created) 
    
    
    def test_category_update_view(self):
        category_name = 'Category'
        category = Category.objects.create(name=category_name, author=self.user)
        
        self.assertEqual(category.name, category_name)
        self.assertEqual(category.author, self.user)
        
        update_category_name = 'othercategory'
        
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('todo:category_edit', kwargs={'pk': category.id}), {'name': update_category_name})
        
        update_category = Category.objects.get(id=category.id)
        
        self.assertEqual(update_category.name, update_category_name)
        self.assertEqual(update_category.author, self.user)

    
    def test_category_update_view_user_not_authenticated(self):
        category_name = 'Category'
        category = Category.objects.create(name=category_name, author=self.user)
        
        self.assertEqual(category.name, category_name)
        self.assertEqual(category.author, self.user)
        
        update_category_name = 'othercategory'
        
        self.client.post(reverse('todo:category_edit', kwargs={'pk': category.id}), {'name': update_category_name})
        
        update_category = Category.objects.get(id=category.id)
        
        self.assertNotEqual(update_category.name, update_category_name)
        self.assertEqual(update_category.author, self.user)

        
    def test_category_delete_view(self):
        category_name = 'Category'
        category = Category.objects.create(name=category_name, author=self.user)
        
        self.assertEqual(category.name, category_name)
        self.assertEqual(category.author, self.user)
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todo:category_delete', kwargs={'pk': category.id}))
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Category.objects.filter(pk=category.pk).exists())
     
        
    def test_category_delete_view_user_not_authenticated(self):
        category_name = 'Category'
        category = Category.objects.create(name=category_name, author=self.user)
        
        self.assertEqual(category.name, category_name)
        self.assertEqual(category.author, self.user)
        
        response = self.client.post(reverse('todo:category_delete', kwargs={'pk': category.id}))

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(pk=category.pk).exists())
        


class TaskViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category', author=self.user)


    def test_task_list_view(self):
        task_1 = Task.objects.create(title='Task1', description= "Test Task", category=self.category, author=self.user)
        task_2 = Task.objects.create(title='Task2', description= "Test Task 2", category=self.category, author=self.user)
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('todo:task_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(set(response.context["tasks"]), set([task_1, task_2]))
        self.assertTemplateUsed(response, 'task_list.html')
     
     
    def test_task_create_view_with_category(self):
        task_title = 'task1'
        task_description =  'test tesk'
        
        data = {
            'title': task_title,
            'description': task_description,
            'category': self.category.id
        }
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todo:task_create'), data)
        
        latest_task_created = Task.objects.last()
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(latest_task_created.title, task_title)
        self.assertEqual(latest_task_created.description, task_description)
        self.assertEqual(latest_task_created.category, self.category)
        self.assertEqual(latest_task_created.author, self.user)
        
        
    def test_task_create_view_with_null_category(self):
        task_title = 'task1'
        task_description =  'test tesk'
        
        data = {
            'title': task_title,
            'description': task_description,
        }
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todo:task_create'), data)
        
        latest_task_created = Task.objects.last()
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(latest_task_created.title, task_title)
        self.assertEqual(latest_task_created.description, task_description)
        self.assertEqual(latest_task_created.category, None)
        self.assertEqual(latest_task_created.author, self.user)
    
    
    def test_task_create_view_with_invalid_data(self):
        task_title = 'task1'
        
        data = {
            'title': task_title,
            'category': self.category.id
        }
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todo:task_create'), data)
        form = response.context["form"]
        
        latest_task_created = Task.objects.last()

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], ['This field is required.'])
        self.assertIsNone(latest_task_created) 
    
    
    def test_task_update_view(self):
        task_title = 'task1'
        task_description =  'test tesk'
    
        task = Task.objects.create(title=task_title, description=task_description, category=self.category, author=self.user)

        self.assertEqual(task.title, task_title)
        self.assertEqual(task.description, task_description)
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.author, self.user)
        
        update_task_name = 'other task'
        data = {    
            'title': 'other task',
            'description': task_description,
            'category': self.category.id
        }
        
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('todo:task_edit', kwargs={'pk': task.id}), data)
                
        update_task = Task.objects.get(id=task.id)
        
        self.assertEqual(update_task.title, update_task_name)
        self.assertEqual(update_task.description, task_description)
        self.assertEqual(update_task.category, self.category)
        self.assertEqual(update_task.author, self.user)
        
        
    def test_task_update_view_user_not_authenticated(self):
        task_title = 'task1'
        task_description =  'test tesk'
    
        task = Task.objects.create(title=task_title, description=task_description, category=self.category, author=self.user)

        self.assertEqual(task.title, task_title)
        self.assertEqual(task.description, task_description)
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.author, self.user)
        
        update_task_name = 'other task'
        data = {    
            'title': 'other task',
            'description': task_description,
            'category': self.category.id
        }
        
        self.client.post(reverse('todo:task_edit', kwargs={'pk': task.id}), data)
                
        update_task = Task.objects.get(id=task.id)
        
        self.assertNotEqual(update_task.title, update_task_name)
        self.assertEqual(update_task.description, task_description)
        self.assertEqual(update_task.category, self.category)
        self.assertEqual(update_task.author, self.user)
    
    
    def test_task_with_null_category(self):
        task_title = 'task1'
        task_description =  'test tesk'
    
        task = Task.objects.create(title=task_title, description=task_description, author=self.user)

        self.assertEqual(task.title, task_title)
        self.assertEqual(task.description, task_description)
        self.assertEqual(task.category, None)
        self.assertEqual(task.author, self.user)
        
        update_task_name = 'other task'
        data = {    
            'title': 'other task',
            'description': task_description,
            'category': self.category.id
        }
        
        self.client.login(username='testuser', password='testpassword')
        self.client.post(reverse('todo:task_edit', kwargs={'pk': task.id}), data)
                
        update_task = Task.objects.get(id=task.id)
        
        self.assertEqual(update_task.title, update_task_name)
        self.assertEqual(update_task.description, task_description)
        self.assertEqual(update_task.category, self.category)
        self.assertEqual(update_task.author, self.user)
        
        
    def test_task_delete_view(self):
        task_title = 'task1'
        task_description =  'test tesk'        
        task = Task.objects.create(title=task_title, description=task_description, category=self.category, author=self.user)
        
        self.assertEqual(task.title, task_title)
        self.assertEqual(task.description, task_description)
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.author, self.user)
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('todo:task_delete', kwargs={'pk': task.id}))
        
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=task.id).exists())
        
        
    def test_task_delete_view_user_not_authenticated(self):
        task_title = 'task1'
        task_description =  'test tesk'        
        task = Task.objects.create(title=task_title, description=task_description, category=self.category, author=self.user)
        
        self.assertEqual(task.title, task_title)
        self.assertEqual(task.description, task_description)
        self.assertEqual(task.category, self.category)
        self.assertEqual(task.author, self.user)
        
        response = self.client.post(reverse('todo:task_delete', kwargs={'pk': task.id}))
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(id=task.id).exists())
   

