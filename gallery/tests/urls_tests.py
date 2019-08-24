from django.test import SimpleTestCase
from django.urls import reverse, resolve

from gallery.views import (
    StudioGallery,
    GuestSpot,
    FameWall,
    studio_photos,
)


class TestGalleryUrls(SimpleTestCase):
    def test_galleries_url_resolves(self):
        url = reverse('gallery:galleries')
        self.assertEqual(resolve(url).func.view_class, StudioGallery)

    def test_guest_spot_url_resolves(self):
        url = reverse('gallery:guest_spot')
        self.assertEqual(resolve(url).func.view_class, GuestSpot)

    def test_wall_of_fame_url_resolves(self):
        url = reverse('gallery:wall_of_fame')
        self.assertEqual(resolve(url).func.view_class, FameWall)

    def test_old_studio_url_resolves(self):
        url = reverse('gallery:gallery_studio', args=['old'])
        self.assertEqual(resolve(url).func, studio_photos)

    def test_new_studio_url_resolves(self):
        url = reverse('gallery:gallery_studio', args=['new'])
        self.assertEqual(resolve(url).func, studio_photos)
