from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from catalog.models import Produto,Categoria

class CategoriaTestCase(TestCase):

    def setUp(self):
        self.categoria = mommy.make(Categoria)

    def test_get_absolute_url(self):
        self.assertEquals(
        self.categoria.get_absolute_url(),
        reverse('catalog:categoria',kwargs={'slug':self.categoria.slug})
        )

class ProdutoTestCase(TestCase):

    def setUp(self):
        self.produto = mommy.make(Produto,slug='produto')

    def test_get_absolute_url(self):
        self.assertEquals(
        self.produto.get_absolute_url(),
        reverse('catalog:produto',kwargs={'slug':self.produto.slug})
        )