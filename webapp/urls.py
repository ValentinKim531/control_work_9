from django.urls import path

from webapp.views.base import GalleryListView
from webapp.views.gallery import PhotoCreateView, PhotoUpdateView, PhotoDeleteView, PhotoDetailView

urlpatterns = [
    path("", GalleryListView.as_view(), name='index'),
    path('gallery/add', PhotoCreateView.as_view(), name='photo_create'),
    path('gallery/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('gallery/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('gallery/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]