from django.test import Client,TestCase

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reversed('home')

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'index.html')
