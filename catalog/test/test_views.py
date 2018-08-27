from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy

from catalog.models import Produto


class ProdutoIndexView(TestCase):

    def setUp(self):
        self.url = reverse('catalog:produtos')
        self.produtos = mommy.make(Produto, _quantity=10)

    def tearDown(self):
        Produto.objects.all().delete()

    def test_status_code_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'catalog/products.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('produtos' in response.context)
        produtos = response.context['produtos']
        self.assertEquals(produtos.count(),3)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages,4)

    def test_page_not_found(self):
        response = self.client.get('{}?page=5'.format(self.url))
        self.assertEquals(response.status_code,404)




