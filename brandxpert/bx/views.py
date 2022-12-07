from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail

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
    fname = request.POST.get('name', '')
    lname = request.POST.get('lname', '')
    number = request.POST.get('number', '')
    #concatenate fname, lname and number to a variable to used as mail subject
    mail_subject = fname + " " + lname + " " + number
    #assing mail subject to subject variable
    subject = mail_subject
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['youngpainzw@gmail.com'])
        except BadHeaderError:
            bad_header_context = {
                "error": "Error sending email, try again!"
            }
            return render(request, "contact/contact.html", bad_header_context)
        sent_context = {
            "200OK": "Email Sent"
        }
        return render(request, "contact/contact.html", sent_context)
    else:
        # render error notification
        error_context = {
            "400": "Make sure all fields are entered and valid"
        }
        return render(request, "contact/contact.html", error_context)
