from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from .forms import write


# Create your views here.
def index(request):
    """ Landing page/home page """
    context = {
        "title": "Home | Brandxperts",
        "GIT": "Get in touch with bx today!"
    }
    return render(request, "index/index.html", context)


def services(request):
    """ Services page """
    context = {
        "title": "Services | Brandxperts",
        "header_name": "Our Services"
    }
    return render(request, "services/services.html", context)


def about(request):
    """ about page """
    context = {
        "title": "About | Brandxperts",
        "header_name": "About us"
    }
    return render(request, "about/about.html", context)


def contact(request):
    """ contact page """
    context = {
        "title": "Contact | Brandxperts",
        "header_name": "Contact us"
    }
    return render(request, "contact/contact.html", context)


def write_form(request):
    """ Get form data and send email """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        #populate/bind the form with request data from the html
        form = write(request.POST)
        #check to see if form is valid
        if form.is_valid():
            #initialize the subject value
            subject = "Website User Inquiry"
            #get data from the post method and assign to the body variable
            body = {
                'info': form.cleaned_data['info'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
                }
            #store data from the body variable into message with a new line after each element
            message = "\n".join(body.values())
            sender = settings.EMAIL_HOST_USER
            receiver = [settings.EMAIL_HOST_USER]
            try:
                #send email
                send_mail(subject, message, sender, receiver)
            except BadHeaderError:
                #catch header error
                context = {"notification": "Error try again"}
                return render(request, "contact/contact.html", context)
            #return the contact page is succesful and display thank you message
            context = {"notification": "Thank you for your message"}
            return render(request, "contact/contact.html", context)
    else:
        #else if not a POST method return empty form back to the user
        form = write()
        return render(request, "contact/contact.html")
