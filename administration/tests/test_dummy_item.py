from django.test import TestCase

# Create your tests here.

class HelloWorldTestCase(TestCase):
    def test_hello_world(self):
        response = self.client.get('/')

        helloWorld = None
        for data in response.json():
            if data['description'] == 'Hello World':
                helloWorld = data
                break

        self.assertEqual(response.status_code, 200)
        self.assertEqual(helloWorld['description'], "Hello World")