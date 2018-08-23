from django.contrib import admin
from .models import Produto,Categoria

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug','created','modified']
    search_fields = ['nome','slug']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug','categoria','created','modified']
    search_fields = ['nome','slug','categoria__nome']



admin.site.register(Produto,ProductAdmin)
admin.site.register(Categoria,CategoryAdmin)
