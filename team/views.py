from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Artist


# Create your views here.
class TeamList(ListView):
    template_name = "team/team_list.html"
    queryset = Artist.objects.order_by('priority','-slug')


class ArtistProfile(DetailView):
    template_name = "team/team_detail.html"


    def get_queryset(self):
        return Artist.objects.filter(slug=self.kwargs['artist'])