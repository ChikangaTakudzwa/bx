import pytest
from django.urls import reverse


# Create your tests here.
@pytest.mark.django_db
def test_home(client):
    """ Test for home page """
    url = reverse("index")
    resp = client.get(url)
    assert resp.status_code == 200

def test_services(client):
    """ Test for services page """
    url = reverse("services")
    resp = client.get(url)
    assert resp.status_code == 200

def test_contact(client):
    """ Test for contact """
    url = reverse("contact")
    resp = client.get(url)
    assert resp.status_code == 200

def test_about(client):
    """ Test for about page """
    url = reverse("about")
    resp = client.get(url)
    assert resp.status_code == 200
