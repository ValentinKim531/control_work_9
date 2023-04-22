from django.views.generic import ListView

from webapp.models import Gallery


class GalleryListView(ListView):
    template_name = 'gallery_list.html'
    model = Gallery
    context_object_name = 'photos'

