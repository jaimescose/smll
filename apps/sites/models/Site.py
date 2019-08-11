from django.db import models

class Site(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()g
    visitors = models.IntegerField()

    def __str__(self):
        return self.title