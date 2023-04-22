from django import forms

from webapp.models import Gallery


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ('photo', 'signature')


class GalleryUpdateForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ('photo', 'signature')

