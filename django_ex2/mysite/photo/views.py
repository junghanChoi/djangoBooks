from django.views.generic import ListView
from django.views.generic import DetailView
from photo.models import Album, Photo

# Create your views here.

class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo
