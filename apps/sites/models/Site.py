from django.db import models
import requests
from bs4 import BeautifulSoup 
from django.conf import settings

class Site(models.Model):
    title = models.CharField(max_length=200, default = 'No title')
    url = models.URLField()
    visitors = models.IntegerField(default = 0)

    def __str__(self):
        return self.url

    @classmethod
    def register_new_site(cls, url):
        try:
            site = cls.objects.get(url = url)
        except Site.DoesNotExist:
            response = requests.get(url)
            html = response.content

            soup = BeautifuSoup(html)

            title = soup.title.string

            site_dict = {
                'title': title,
                'url': url
            }

            site = cls.objects.create(**site_dict)

        short_url = '/'.join([settings.DOMAIN, 'site', str(site.id)])

        return short_url


