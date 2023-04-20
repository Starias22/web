from django.test import SimpleTestCase

# Create your tests here.

#OUr app doesn't use any database
class Tests(SimpleTestCase):
    def testHomePage(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)
    def testAboutPage(self):
        response=self.client.get('/about/')
        self.assertEqual(response.status_code,200)
