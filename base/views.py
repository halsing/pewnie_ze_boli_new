from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail
from django.core.paginator import Paginator
from django.views.generic import ListView

from .forms import ContactForm
from .views_helper import FAQ
from team.models import Artist

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():

            recipient_list = [
                'pewniezeboli@gmail.com',
                'pewniezeboli2@gmail.com'
            ]

            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            phone_number = form.cleaned_data['phone_number']
            preferred_contact = form.cleaned_data['preferred_contact']
            tatoo_place = form.cleaned_data['tatoo_place']
            tatoo_size = form.cleaned_data['tatoo_size']
            tatoo_maker = form.cleaned_data['tatoo_maker']
            description = form.cleaned_data['description']
            attach = request.FILES.getlist('attach', False)

            # send_mail(name, from_email, phone_number, recipient_list)
            # send_mail ('subject', 'body of the message', 'noreply@parsifal.co', ['vitorfs@gmail.com'])

            body = f"\
                Imię: {name}\n \
                E-mail: {from_email}\n \
                Numer telefonu: {phone_number}\n \
                Preferowany rodzaj kontaktu: {preferred_contact}\n \
                Miejsce tatuażu: {tatoo_place}\n \
                Wielkość tatuażu: {tatoo_size}\n \
                Tatuator / Piercer: {tatoo_maker}\n \
                Opis:\n {description} \
                "

            name = f"Formularz tattoo od: {name}"
            mail = EmailMessage(name, body, from_email, recipient_list)
            if attach:
                for i in attach:
                    mail.attach(i.name, i.read(), i.content_type)
            mail.send()
            # return render(request, 'pewniezeboli/index.html')
    else:
        form = ContactForm()
    return render(request, "base/contact.html", {'form': form})


def faq(request):
    context = {
        'faq': FAQ,
    }
    return render(request, "base/faq.html",context)


class Home(ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = "base/index.html"

def index(request):
    return render(request, "base/index.html")


def laser(request):
    return render(request, "base/laser.html")


# class Guides(ListView):
#     model = Guide


def guides(request):
    return render(request, "base/guides.html")