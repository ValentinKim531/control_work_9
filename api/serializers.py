from rest_framework import serializers

from webapp.models import Gallery


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        exclude = ('created_at', 'signature')
