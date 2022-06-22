from django.urls import path
from .views import AddAlbums


urlpatterns=[
    # path('user/authorization/', UserAuthorization.as_view(), name="Authorization"),
    path('album/', AddAlbums.as_view(), name="Album"),
]