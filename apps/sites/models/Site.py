from django.db import models
import requests
from bs4 import BeautifulSoup 
from django.conf import settings

class Site(models.Model):
    title = models.CharField(max_length=200, default = 'No title')
    url = models.URLField()
    short_url = models.URLField(default = None, null = True)
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

            soup = BeautifulSoup(html, 'html.parser')

            title = soup.title.string

            site_dict = {
                'title': title,
                'url': url
            }

            site = cls.objects.create(**site_dict)

        if site.short_url:
            short_url = site.short_url
        else:
            short_url = '/'.join([settings.DOMAIN, 'site', str(site.id)])

            site.short_url = short_url
            
            site.save()
        
        return site


