from django.test import Client,TestCase
from django.urls import reverse
from django.core import mail


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('home')

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response,'index.html')

class ContactViewTesCase(TestCase):

    def setUp(self):
        self.url = reverse('contato')

    def test_status_code_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_error(self):
        data = {'name':'','message':'','email':''}
        response = self.client.post(self.url,data)
        self.assertFormError(response,'form','name','Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email','Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message','Este campo é obrigatório.')


    def test_form_ok(self):
        data = {'name': 'teste', 'message': 'teste', 'email': 'test@teste.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['sucess'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do Django E-commerce')