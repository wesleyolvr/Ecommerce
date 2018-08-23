from django.db import models
from django.urls import reverse


class Categoria(models.Model):

    nome = models.CharField('name',max_length=100)
    slug = models.SlugField('identificador',max_length=100)

    created = models.DateTimeField('criado em',auto_now_add=True)
    modified = models.DateTimeField('modificado em ',auto_now_add=True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural = 'Categorias'
        ordering= ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalog:categoria',kwargs= {'slug':self.slug})


class Produto(models.Model):

    nome = models.CharField('nome',max_length=100)
    slug = models.SlugField('identificador',max_length=100)
    categoria = models.ForeignKey(Categoria,verbose_name='Categoria',on_delete=models.CASCADE)
    descricao = models.TextField('Descrição',blank=True)
    preco = models.DecimalField('Preço', decimal_places=2,max_digits=8)

    created = models.DateTimeField('criado em',auto_now_add=True)
    modified = models.DateTimeField('modificado em ',auto_now_add=True)

    class Meta:
        verbose_name='Produto'
        verbose_name_plural = 'Produtos'
        ordering= ['nome']

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('catalog:produto',kwargs= {'slug':self.slug})


