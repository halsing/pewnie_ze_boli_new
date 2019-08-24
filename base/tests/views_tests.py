from django.test import TestCase, Client
from django.urls import reverse


class TestHomeView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_response_GET(self):
        response = self.client.get(reverse('base:index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/index.html')


class TestContactView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_contact_response_GET(self):
        response = self.client.get(reverse('base:contact'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/contact.html')


class TestFaqView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_faq_response_GET(self):
        response = self.client.get(reverse('base:faq'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/faq.html')


class TestLaserView(TestCase):
    def test_laser_response_GET(self):
        response = self.client.get(reverse('base:laser'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/laser.html')
