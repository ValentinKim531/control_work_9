from django.contrib import admin

from webapp.models import Gallery, Favorite


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['photo', 'signature', 'author', 'created_at']
    ordering = ['created_at']


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['photo', 'user']


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Favorite, FavoriteAdmin)


