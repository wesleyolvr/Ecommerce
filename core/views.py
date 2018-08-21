from django.shortcuts import render


def index(request):
    texts = ['helou brotheragem',
             'tudo bom com você?',
             'eu estou bem!',
             'e você?', 'tambem estou']
    context = {
        'texts': texts,
        'title': 'django e-commerce',
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')


def product_list(request):
    return render(request, 'products.html')
