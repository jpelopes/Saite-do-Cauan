from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fotografia', views.albums, name='albums'),
    path('fotografia/<int:album_id>', views.album, name='album'),
    path('desenhos', views.drawings, name='drawings'),
    path('desenhourbano', views.urbandrawings, name='urbandrawings'),
    path('contato', views.contact, name='contact'),
    path('bio', views.bio, name='bio')
]
