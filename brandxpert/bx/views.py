from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title" : "Home | Brandxperts",
        "GIT" : "Get in touch with bx today!"
    }
    return render(request, "index/index.html", context)

def services(request):
    context = {
        "title" : "Services | Brandxperts"
    }
    return render(request, "services/services.html", context)