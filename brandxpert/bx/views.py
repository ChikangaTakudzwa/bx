from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .forms import write


# Create your views here.
def index(request):
    context = {
        "title": "Home | Brandxperts",
        "GIT": "Get in touch with bx today!"
    }
    return render(request, "index/index.html", context)


def services(request):
    context = {
        "title": "Services | Brandxperts",
        "header_name": "Our Services"
    }
    return render(request, "services/services.html", context)


def about(request):
    context = {
        "title": "About | Brandxperts",
        "header_name": "About us"
    }
    return render(request, "about/about.html", context)


def contact(request):
    context = {
        "title": "Contact | Brandxperts",
        "header_name": "Contact us"
    }
    return render(request, "contact/contact.html", context)


def write_form(request):
    """ Get from data and send email """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = write(request.POST)
        if form.is_valid():
            subject = "Website User Inquiry"
            body = {
                'info': form.cleaned_data['info'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
                }
            message = "\n".join(body.values())
            sender = settings.EMAIL_HOST_USER
            receiver = [settings.EMAIL_HOST_USER]
            try:
                send_mail(subject, message, sender, receiver)
            except BadHeaderError:
                context = {"notification": "Error try again"}
                return render(request, "contact/contact.html", context)
            context = {"notification": "Thank you for your message"}
            return render(request, "contact/contact.html", context)
    else:
        form = write()
        return render(request, "contact/contact.html")
