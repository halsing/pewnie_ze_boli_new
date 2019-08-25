from django.test import TestCase
from io import BytesIO
from PIL import Image
from django.core.files.base import File

from team.models import Artist, ArtistPhoto


def create_test_image(
        name='test.jpg', ext='JPEG', size=(1600, 1550), color=(256, 0, 0)):
    file_obj = BytesIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


class TestArtistModels(TestCase):

    def setUp(self):
        self.artist1 = Artist.objects.create(
            name='test1',
            style='test1',
            description='bla bla',
            artist_type='T',
            photo=create_test_image()
        )

    def test_artist_slug_created(self):
        self.assertEqual(self.artist1.slug, 'test1')

    def test_photo_min_size(self):
        self.assertEqual(self.artist1.photo_min.width, 600)

    def test_photo_medium_size(self):
        self.assertEqual(self.artist1.photo_medium.width, 900)


class TestArtistPhoto(TestCase):

    def setUp(self):
        self.artist1 = Artist.objects.create(
            name='test1',
            style='test1',
            description='bla bla',
            artist_type='T',
            photo=create_test_image()
        )

        self.photo1 = ArtistPhoto.objects.create(
            artist=self.artist1,
            photo=create_test_image()
        )

    def test_artist_photo_foreignkey(self):
        self.assertEqual(self.photo1.artist.name, 'test1')

    def test_artist_photo_photo_min_size(self):
        self.assertEqual(self.artist1.photo_min.width, 600)

    def test_artist_photo_photo_medium_size(self):
        self.assertEqual(self.artist1.photo_medium.width, 900)
