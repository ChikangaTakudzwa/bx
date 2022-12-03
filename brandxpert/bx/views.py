from django.shortcuts import render

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
