from django.views import View
from django.core import serializers
import json
from django.shortcuts import redirect, render
from django.http import HttpResponse

from apps.sites.models.Site import Site

class SiteView(View):
    def get(self, request, *args, **kwargs):
        sites = Site.objects.all()
        serialized_queryset = serializers.serialize('json', sites)

        response = HttpResponse(serialized_queryset)

        return response

    def post(self, request, *args, **kwargs):
        body = request.body
        url = body.get('url')

        site = Site.register_new_site(url)

        serialized_queryset = serializers.serialize('json', [site, ])

        response = HttpResponse(serialized_queryset)

        return response
