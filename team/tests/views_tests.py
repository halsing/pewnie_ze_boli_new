from django.test import TestCase, Client
from django.urls import reverse

from .models_tests import create_test_image
from team.views import ArtistProfile
from team.models import Artist, ArtistPhoto


class TestTeamListView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_base_response_GET(self):
        response = self.client.get(reverse('team:team_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'team/team_list.html')


# class TestArtistProfileListView(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#
#     def test_base_response_GET(self):
#
#      # response=ArtistProfile.as_view()(self.instance.request,slug="the_book")
#
#         response = self.client.get(
#             reverse('base:artist_profile', kwargs={'artist': "test"}))
#
#         self.assertEquals(response.status_code, 404)
#         # self.assertTemplateUsed(response, 'team/team_detail.html')
