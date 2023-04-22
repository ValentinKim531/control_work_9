from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.forms import GalleryForm, GalleryUpdateForm
from webapp.models import Gallery
from django.contrib.auth.mixins import LoginRequiredMixin

class PhotoDetailView(DetailView):
    template_name = 'photo_detail.html'
    model = Gallery
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='photo_update').exists():
            context['has_update_permission'] = True
        if self.request.user.groups.filter(name='photo_del').exists():
            context['has_del_permission'] = True
        return context


class PhotoCreateView(CreateView):
    template_name = 'photo_create.html'
    model = Gallery
    form_class = GalleryForm
    success_url = '/'

    def form_valid(self, form):
        self.object: Gallery = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'photo_update.html'
    model = Gallery
    form_class = GalleryUpdateForm
    context_object_name = 'photos'

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not (self.get_object().author == request.user or request.user.groups.filter(name='photo_update').exists()):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Gallery
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not (self.get_object().author == request.user or request.user.groups.filter(name='photo_delete').exists()):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)



