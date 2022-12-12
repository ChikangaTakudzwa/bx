import pytest
from django.urls import reverse
# from django.core import mail


# Create your tests here.
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


@pytest.mark.django_db
def test_portfolio(client):
    """ Test for portfolio page """
    url = reverse("portfolio")
    resp = client.get(url)
    assert resp.statuc_code == 200


# def test_email_send(client):
#     """ Test for sending emails """
#     mail.send_mail(
#         'Takudzwa Chikanga 771034920',
#         'Wasuup',
#         'tornado@bx.com',
#         ['dreamchaser@bx.com'],
#         fail_silently=False,
#     )
#     assert len(mail.outbox)
