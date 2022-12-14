from django.urls import path
from . import views

# url paths for the app
urlpatterns = [
    path('', views.index, name="index"),
    path('services/', views.services, name="services"),
    path('services/<str:param>', views.services, name="services"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('write/', views.write_form, name="write"),

]
