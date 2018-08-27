from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings



def index(request):
    context = {
        'texts': ['eai brotheragem', 'beleza?']
    }
    return render(request, 'index.html', context)


def contact(request):
    sucess=False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        sucess = True

    context = {
        'form': form,
        'sucess':sucess
    }
    return render(request, 'contact.html', context)
