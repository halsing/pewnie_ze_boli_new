from django.test import TestCase, Client
from django.urls import reverse


class TestGalleriesView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_base_response_GET(self):
        response = self.client.get(reverse('gallery:galleries'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/studio_gallery.html')


class TestGuestSpotView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_base_response_GET(self):
        response = self.client.get(reverse('gallery:guest_spot'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/guest_spot.html')


class TestFameWallView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_base_response_GET(self):
        response = self.client.get(reverse('gallery:wall_of_fame'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/fame_wall.html')


class TestGalleryStudioView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_old_studio_response_GET(self):
        response = self.client.get(reverse(
            'gallery:gallery_studio',
            args=['old'],
        ))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/studio_photos.html')

    def test_new_studio_response_GET(self):
        response = self.client.get(reverse(
            'gallery:gallery_studio',
            args=['new'],
        ))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/studio_photos.html')

    def test_fail_name_studio_response_GET(self):
        response = self.client.get(reverse(
            'gallery:gallery_studio',
            args=['fake'],
        ))

        self.assertEquals(response.status_code, 404)
        self.assertTemplateNotUsed(response, 'gallery/studio_photos.html')
