from django.test import TestCase
from administration.models import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            name='test',
            email='test@example.com',
        )
        self.assertEqual(user.name, 'test')
        self.assertEqual(user.email, 'test@example.com') 

    def test_user_str(self):
        user = User.objects.create(email='test@example.com')  
        email = 'test@example.com' 
        self.assertEqual(str(user), email)  
        