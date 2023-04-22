from django.urls import path, include
from rest_framework import routers
from api.views import PhotoApiView

router = routers.DefaultRouter()
router.register('photo', PhotoApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('photo/<int:pk>/to_favorite/', PhotoApiView.as_view({'get': 'photo_to_favorite'})),
    path('photo/<int:pk>/from_favorite/', PhotoApiView.as_view({'get': 'photo_from_favorite'})),
]
