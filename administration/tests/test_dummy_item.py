from django.test import TestCase

# Create your tests here.

class HelloWorldTestCase(TestCase):
    def test_hello_world(self):
        response = self.client.get('/')

        helloWorldIndex = 0
        for data in response.json():
            if data['description'] == 'Hello World':
                break
            
            helloWorldIndex += 1

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[helloWorldIndex]['description'], "Hello World")