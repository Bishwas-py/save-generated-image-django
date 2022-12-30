from django.contrib import admin

from records.models import Website

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'screenshot')

admin.site.register(Website, WebsiteAdmin)