from django.views.generic import dates
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from preps.apps.photos.models import PhotoGallery

class GalleryList(ListView):
    '''
    Defines a function which provides a list view of photo galleries.
    '''
    context_object_name = "galleries"
    queryset = PhotoGallery.objects.filter(active=True).select_related()
    template_name = 'photos/gallery_list.html'
    
class GalleryDetail(DetailView):
    '''
    Defines a function which provides a detail view of photo galleries.
    '''
    context_object_name = "gallery"
    model = PhotoGallery
    template_name = 'photos/gallery_detail.html'
    
    # Time to override the get_queryset function to find our one post.
    def get_queryset(self):
        '''
        Defines a function which returns a queryset to build the detail view from.
        '''
        # Let's return only the post which matches on id (pk from the URL) and slug (slug from the URL).
        return PhotoGallery.objects.filter(id=self.kwargs['pk'], slug=self.kwargs['gallery_slug'])
    
