from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from api.serializers import PhotoSerializer
from webapp.models import Gallery


class PhotoApiView(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = PhotoSerializer

    def photo_to_favorite(self, request, *args, **kwargs):
        photo_pk = self.get_object()
        user_from_request = request.user
        user_from_request.favorited_photos.add(photo_pk)
        return JsonResponse({'key': 'to favorite'})

    def photo_from_favorite(self, request, *args, **kwargs):
        photo_pk = self.get_object()
        user_from_request = request.user
        user_from_request.favorited_photos.remove(photo_pk)
        return JsonResponse({'key': 'from favorite'})

