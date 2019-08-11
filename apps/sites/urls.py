from django.urls import path
from apps.sites.views import SiteView

urlpatterns = [
    path('', SiteView.as_view(), name='site_view'),
]