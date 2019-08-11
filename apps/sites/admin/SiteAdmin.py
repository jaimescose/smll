from django.contrib import admin
from apps.sites.models.Site import Site
from django.conf import settings

def create_qr_code(modeladmin, request, queryset):
    for site in queryset:
        url = site.generate_qr_code()
        url.svg(str(site.id) + '.svg', scale=8)

create_qr_code.short_description = "Generate QRcode for selected sites"

def migrate_short_urls_to_new_domain(modeladmin, request, queryset):
    for site in queryset:
        site.change_short_url_domain()

migrate_short_urls_to_new_domain.short_description = 'Migrate selected sites to new domain'

class SiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'short_url', 'visitors']
    ordering = ['title']
    actions = [create_qr_code, migrate_short_urls_to_new_domain]

admin.site.register(Site, SiteAdmin)
