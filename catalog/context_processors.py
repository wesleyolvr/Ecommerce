from .models import Categoria

def categoria(request):
    context ={
        'categorias' : Categoria.objects.all()
    }
    return context
