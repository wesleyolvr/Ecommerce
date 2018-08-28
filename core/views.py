from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import View, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

index = IndexView.as_view()


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
