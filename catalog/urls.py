from django.urls import path
from .views import product_list,categoria
urlpatterns = [
    path('',product_list,name='produtos'),
    path('<slug:slug>/',categoria,name='categoria')
]