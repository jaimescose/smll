from django.db import models

class Site(models.Model):
    title = models.CharField(max_length=200, default = 'No title')
    url = models.URLField()
    visitors = models.IntegerField(default = 0)

    def __str__(self):
        return self.url