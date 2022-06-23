from django.urls import path
from spotapp import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns=[
    # path('user/authorization/', UserAuthorization.as_view(), name="Authorization"),
    path('album/', views.AddAlbums.as_view(), name="Add Album"),
    path('get_albums/', views.FindAlbums.as_view(), name='Find Albums'),
    path('album_tracks/', views.AlbumTrack.as_view(), name="Tracks"),
    path('get_releases/', views.NewRelease.as_view(), name='New Releases'),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refres_token'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify_token')
]