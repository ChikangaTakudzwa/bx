from django.shortcuts import render

# Create your views here.
def index(requests):
    context = {
        "title" : "Home | Brandxperts"
    }
    return render(request, "base.html", context)