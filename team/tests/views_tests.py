from django.test import TestCase, Client
from django.urls import reverse
from team.views import ArtistProfile


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
#         # response = ArtistProfile.as_view()(self.instance.request,slug="the_book")
#         response = self.client.get(reverse('base:artist_profile', kwargs={'artist':1}))
#
#         self.assertEquals(response.status_code, 404)
#         # self.assertTemplateUsed(response, 'team/team_detail.html')
