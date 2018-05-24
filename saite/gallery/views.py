from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

from .models import Album, Photo, Contact, Settings, Page, Bio

def index(request):
    template = loader.get_template('gallery/home.html')

    settings = None
    page = Page.objects.filter(name='home')
    if page:
        if page[0].settings:
            settings = page[0].settings

    context = {
        'settings': settings
    }
    
    return HttpResponse(template.render(context, request))

def albums(request):
    template = loader.get_template('gallery/albums.html')

    settings = None
    page = Page.objects.filter(name='albums')
    if page:
        if page[0].settings:
            settings = page[0].settings

    context = {
        'albums': Album.objects.all(),
        'settings': settings
    }
    
    return HttpResponse(template.render(context, request))

def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    photos = album.photo_set.all()
    template = loader.get_template('gallery/album.html')
    context = {
        'album': album,
        'photos': photos
    }

    return HttpResponse(template.render(context, request))

def drawings(request):
    return HttpResponse("Drawings page")

def urbandrawings(request):
    return HttpResponse("Drawings page")

def contact(request):
    template = loader.get_template('gallery/contact.html')
    context = {
        'contacts': Contact.objects.all()
    }

    return HttpResponse(template.render(context, request))

def bio(request):
    template = loader.get_template('gallery/bio.html')
    context = {
        'bio': Bio.objects.all()
    }

    return HttpResponse(template.render(context, request))
