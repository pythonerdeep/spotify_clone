from django.urls import path
from .views import Album


urlpatterns=[
    # path('user/authorization/', UserAuthorization.as_view(), name="Authorization"),
    path('album/', Album.as_view(), name="Album"),
]