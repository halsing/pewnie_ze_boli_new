from django.test import SimpleTestCase
from django.urls import reverse, resolve

from team.views import TeamList, ArtistProfile


class TestTeamUrls(SimpleTestCase):

    def test_artist_profile_url_resolves(self):
        url = reverse('base:artist_profile', args=['test'])
        self.assertEqual(resolve(url).func.view_class, ArtistProfile)

    def test_team_list_url_resolves(self):
        url = reverse('team:team_list')
        self.assertEqual(resolve(url).func.view_class, TeamList)
