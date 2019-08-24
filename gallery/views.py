from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import Http404

from .models import (OldStudioGallery,
                     NewStudioGallery,
                     FameWall,
                     GuestSpotWall)


# Create your views here.
class StudioGallery(TemplateView):
    template_name = "gallery/studio_gallery.html"


class GuestSpot(ListView):
    queryset = GuestSpotWall.objects.order_by("-pk")
    template_name = "gallery/guest_spot.html"


class FameWall(ListView):
    queryset = FameWall.objects.order_by("-pk")
    template_name = "gallery/fame_wall.html"


def studio_photos(request, type):
    if type == 'old':
        gallery = OldStudioGallery.objects.order_by("-pk")
    elif type == 'new':
        gallery = NewStudioGallery.objects.order_by("-pk")
    else:
        raise Http404

    context = {
        'gallery': gallery,
    }

    return render(request, "gallery/studio_photos.html", context)
