from django.db import models
from django.utils import timezone
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.template.defaultfilters import slugify

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# function return path to directory with images with current filename
def get_directory(instance,filename):
    return f"{instance.category}/{filename}"


# Create your models here.
class BasePhoto(models.Model):
    photo = models.ImageField(upload_to=get_directory)
    photo_medium = models.ImageField(upload_to=get_directory,
                                     blank=True,
                                     null=True,
                                     editable=False,
                                     )
    photo_min = models.ImageField(upload_to=get_directory,
                                  blank=True,
                                  null=True,
                                  editable=False,
                                  )

    def save(self, *args, **kwargs):

        # resize the image
        if self.photo:
            self.photo_medium = self.compress_image(self.photo,900,600)
            self.photo_min = self.compress_image(self.photo, 600, 400)

        super(BasePhoto,self).save(*args, **kwargs)

    def compress_image(self,my_image,my_width,my_height):
        img_temp = PILImage.open(my_image)
        x = my_width
        y = my_height
        if img_temp.mode != "RGB":
            img_temp.convert('RGB')

        # get current size of main photo
        width, height = img_temp.size
        ratio = width / height


        if width > x or height > y:
            if width >= height:
                y = int(x / ratio)
            elif height > width:
                x = int(y * ratio)
        else:
            x = width
            y = height

        img_temp.thumbnail((x,y), PILImage.ANTIALIAS)
        save_buff = BytesIO()
        img_temp.save(save_buff,
                     format="JPEG",
                     optimize=True,
                     quality=70
                     )
        save_buff.seek(0)
        my_image = InMemoryUploadedFile(
            save_buff,
            'ImageField',
            "%s.jpg" % self.photo.name.split('.')[0],
            'image/jpeg',
            save_buff.__sizeof__(),
            None
        )
        return my_image

    class Meta:
       abstract = True


class OldStudioGallery(BasePhoto):
    category = 'old_studio'


class NewStudioGallery(BasePhoto):
    category = 'new_studio'


class GuestSpotWall(BasePhoto):
    name = models.CharField(max_length=30,verbose_name="Imię")
    category = 'guest_spot_wall'

    def __str__(self):
        return self.name


class FameWall(BasePhoto):
    name = models.CharField(max_length=30,verbose_name="Imię")
    category = 'fame_wall'

    def __str__(self):
        return self.name


#------------------------ SIGNALS ---------------------------
@receiver(pre_delete, sender=GuestSpotWall)
def mymodel_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
    instance.photo_min.delete(False)
    instance.photo_medium.delete(False)


@receiver(pre_delete, sender=FameWall)
def mymodel_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
    instance.photo_min.delete(False)
    instance.photo_medium.delete(False)
