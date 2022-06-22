from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .spotify_script import *
from .models import Album, Track



# Create your views here.

#### API for find albums from spotify and inserting into db"
class AddAlbums(APIView):
    def get(self,request):
        try:
            header=request.headers
            token=header["Authorization"]
            album_id=request.GET.get("id")
            result=find_album(token,album_id)
            # if result['success'] == False:
            #     return Response(result)
            get_album=result['album']
            # print(get_album)
            ab=Album.objects.create(album_id=get_album['album_id'], album_name=get_album['album_name'], album_url=get_album['album_url'],
                                album_label=get_album['label'], album_type=get_album['album_type'], artist_name=get_album['artists'], 
                                total_tracks=get_album['total_tracks'], release_date=get_album['release_date'])

            get_tracks=result['tracks']
            for track in get_tracks:
                # print(track)
                trac=Track.objects.create(track_id=track['track_id'], track_name=track['track_name'], duration_ms=track['duration'],
                                        artist=track['artist'], track_url=track['url'], album=ab)
            return Response({"message":"Successful", "success":True,})
        except Exception as e:
            return Response({"message": str(e), "success": False})

#### end online api here #####









