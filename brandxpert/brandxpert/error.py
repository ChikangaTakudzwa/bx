from django.shortcuts import render


# def page_not_found_view(request, exception):
#     """ 404 handler view """
#     return render (request, '404.html', status=404)

def page_not_found_view(request):
    """ 404 handler view """
    return render (request, '404.html')
    