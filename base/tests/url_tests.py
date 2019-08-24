from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import contact, faq, Home, Laser


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('base:index')
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_contact_url_resolves(self):
        url = reverse('base:contact')
        self.assertEqual(resolve(url).func, contact)

    def test_faq_url_resolves(self):
        url = reverse('base:faq')
        self.assertEqual(resolve(url).func, faq)

    def test_laser_url_resolves(self):
        url = reverse('base:laser')
        self.assertEqual(resolve(url).func.view_class, Laser)
