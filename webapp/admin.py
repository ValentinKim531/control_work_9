from django.contrib import admin

from webapp.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['photo', 'signature', 'author', 'created_at']
    ordering = ['created_at']


admin.site.register(Gallery, GalleryAdmin)


