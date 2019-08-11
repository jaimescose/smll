from django.test import TestCase
from ..apps.sites.models.Site import Site
from django.conf import settings

class SiteTestCase(TestCase):
    def setUp(self):
        url = 'https://www.google.com/'

    def test_url_shortening(self):
        site = Site.register_new_site(url)
        short_url_expected = '/'.join([settings.DOMAIN, 'site', str(site.id)])
        self.assertEqual(site.short_url, short_url_expected)
