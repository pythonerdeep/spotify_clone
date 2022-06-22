from django.urls import path
from spotapp import views


urlpatterns=[
    # path('user/authorization/', UserAuthorization.as_view(), name="Authorization"),
    path('album/', views.AddAlbums.as_view(), name="Add Album"),
    path('get_albums/', views.FindAlbums.as_view(), name='Find Albums'),
    path('album_tracks/', views.AlbumTrack.as_view(), name="Tracks"),
    path('get_releases/', views.NewRelease.as_view(), name='New Releases'),
]