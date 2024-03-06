from django.test import TestCase
from .models import User
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser

class LoginTestCase(TestCase):
    def setUp(self):
        self.username = 'username'
        self.password = 'password'
        email = 'testuser@example.com'
        self.user = User.objects.create_user(username=self.username, password=self.password, email=email)
    
    
    def test_login_success(self):
        url = reverse('accounts:login')  
        data = {'username': self.username, 'password': self.password}
        
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('todo:task_list'))
        self.assertIsNotNone(response.cookies["sessionid"]) 
  

    def test_login_failure_username_error(self):
        url = reverse('accounts:login') 
        other_username = "other_username"
        data = {'username': other_username, 'password': self.password}
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 200)  
        self.assertNotIn('sessionid', response.cookies)
        with self.assertRaises(AssertionError):
            self.assertRedirects(response, reverse('todo:task_list'))


    def test_login_failure_password_error(self):
        url = reverse('accounts:login') 
        other_password = "other_password"
        data = {'username': self.username, 'password': other_password}
        
        response = self.client.post(url, data)
        
        self.assertEqual(response.status_code, 200)  
        self.assertNotIn('sessionid', response.cookies)
        with self.assertRaises(AssertionError):
            self.assertRedirects(response, reverse('todo:task_list'))
             
            
class SignupTestCase(TestCase):
    def setUp(self):
        self.username = 'username'
        self.password = 'password'
        self.email = 'testuser@example.com'
        self.user = User.objects.create_user(username=self.username, password=self.password, email=self.email)
        
        
    def test_signup_success(self):
        data_signup = {
            'username':'username2',
            'email': 'test@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }

        response = self.client.post(reverse('accounts:signup'), data_signup)
        
        self.assertRedirects(response, reverse('accounts:login'))  
        

    def test_signup_error_username_already_exist(self):
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(reverse('accounts:login')  , data)

        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('todo:task_list'))
        self.assertIsNotNone(response.cookies["sessionid"]) 
        
        data_signup = {
            'username': self.username,
            'email': 'test@example.com',
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }

        response = self.client.post(reverse('accounts:signup'), data_signup)
        form = response.context["form"]
        
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['Um usuário com este nome de usuário já existe.'])
        
        
    def test_signup_error_email_already_exist(self):
        data_signup = {
            'username': 'username34',
            'email': self.email,
            'password1': 'strongpassword123',
            'password2': 'strongpassword123',
        }

        response = self.client.post(reverse('accounts:signup'), data_signup)
        form = response.context["form"]
        
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Usuário com este Endereço de email já existe.'])          
        
        
    def test_signup_error_weak_password(self):       
        data_signup = {
            'username': 'username5',
            'email': 'test25@gmail.com',
            'password1': '123456789',
            'password2': '123456789',
        }

        response = self.client.post(reverse('accounts:signup'), data_signup)
        form = response.context["form"]
        
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['Esta senha é muito comum.', 'Esta senha é inteiramente numérica.'])  
            
             
class LogoutTestCase(TestCase):  
    def test_logout_view(self):
        User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('accounts:logout'))

        self.assertRedirects(response, reverse('accounts:login'))

        


   