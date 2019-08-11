from django.test import TestCase
from ..apps.sites.models.Site import Site

class SiteTestCase(TestCase):
    def setUp(self):
        Site.objects.create(title = 'Google', 
        url = 'https://www.google.com/',
        visitors = 0)