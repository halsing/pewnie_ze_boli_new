from django.db import models
from django.db.models.signals import pre_delete
from django.template.defaultfilters import slugify
from django.dispatch.dispatcher import receiver

from gallery.models import BasePhoto


ARTIST_TYPE = (
    ('T', 'Tattoo'),
    ('P', 'Piercing'),
    ('S', 'Obsługa')
)


# Create your models here.
class Artist(BasePhoto):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField(upload_to="team_logo_img", blank=True, null=True)
    style = models.CharField(max_length=40,
                             verbose_name="Stylistyka prac artysty")
    description = models.CharField(max_length=300,
                                   verbose_name="Krótki opis",
                                   blank=True,
                                   null=True)
    inst_link_name = models.CharField(max_length=100, blank=True, null=True)
    facebook_link_name = models.CharField(max_length=100, blank=True, null=True)
    pzb_gallery = models.TextField(blank=True, null=True)
    priority = models.IntegerField(default=1)
    artist_type = models.CharField(choices=ARTIST_TYPE,
                                   default=ARTIST_TYPE[0],
                                   max_length=1)

    category = "tattoo_artist"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class ArtistPhoto(BasePhoto):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    category = "artist_photo"

    def __str__(self):
        return self.artist


#------------------------ SIGNALS ---------------------------
@receiver(pre_delete, sender=Artist)
def artist_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
    instance.logo.delete(False)
    instance.photo_min.delete(False)
    instance.photo_medium.delete(False)


@receiver(pre_delete, sender=ArtistPhoto)
def artistphoto_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
    instance.photo_min.delete(False)
    instance.photo_medium.delete(False)
