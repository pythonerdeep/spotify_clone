from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .spotify_script import *
from .models import Album, Track
import json
from django.core import serializers
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



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
            return Response({"message":"Albums added successfuly.", "success":True,})
        except Exception as e:
            return Response({"message": str(e), "success": False})

#### end online api here #####

#### API for - Find Albums and several albums##
class FindAlbums(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        try:
            album_id=request.GET.get('id')
            if album_id is None:
                albums_data=Album.objects.all()
                json_data=serializers.serialize('json', albums_data)
                return HttpResponse(json_data, content_type='application/json')
            album_data=Album.objects.filter(album_id=album_id)
            json_data=serializers.serialize('json', album_data)
            return HttpResponse(json_data, content_type='application/json')

        except Exception as e:
            return Response({"message": str(e), "success": False})

##### API for - deleting Album    
    def delete(self,request):
        try:
            album_id=request.data.get('album_id')
            # print(album_id)
            album=Album.objects.get(album_id=album_id)
            album.delete()
            return Response({"message":'Album deleted sucessfully.', 'success':True})
        
        except Exception as e:
            return Response({"message": str(e), "success": False})
        


#### API for - find albums Track
class AlbumTrack(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        try:
            album_id=request.GET.get('id')
            tracks=Track.objects.filter(album__album_id=album_id)
            json_data=serializers.serialize('json', tracks)
            return HttpResponse(json_data, content_type='application/json')
        
        except Exception as e:
            return Response({"message": str(e), "success": False})

#### API for - find new-release
class NewRelease(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        try:
            release=request.GET.get('is_new')
            print(release)
            releases=Album.objects.filter(is_new=release)
            json_data=serializers.serialize('json', releases)
            return HttpResponse(json_data, content_type='application/json')
        
        except Exception as e:
            return Response({"message": str(e), "success": False})











