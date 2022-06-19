from django.urls import path
from .views import Album, SevaralAlbums, AlbumTrack, Release


urlpatterns=[
    # path('user/authorization/', UserAuthorization.as_view(), name="Authorization"),
    path('album/', Album.as_view(), name="Album"),
    path('several_albums/', SevaralAlbums.as_view(), name="Several albums"),
    path('track_album/', AlbumTrack.as_view(), name="Track album"),
    path('new_releases/', Release.as_view(), name="New releases"),
]