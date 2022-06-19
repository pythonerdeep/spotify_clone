from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .spotify_script import *



# Create your views here.
######  api for fetching Album from spotify ########
# class UserAuthorization(APIView):
#     def get(self,request):
#         try:
#             return Response({"message":"ok"})
#         except Exception as e:
#             return Response({"message": str(e), "success": False})


class Album(APIView):
    def get(self,request):
        try:
            header=request.headers
            token=header["Authorization"]
            album_id=request.GET.get("id")
            result=find_album(token,album_id)
            # print("=====",len(result))
            return Response({"message":"Successful", "success":True, "data":result})
        except Exception as e:
            return Response({"message": str(e), "success": False})


    def delete(self,request):
        try:
            header=request.headers
            token=header["Authorization"]
            album_id=request.data.get("album_id")
            result=remove_album(token,album_id)
            return Response(result)
        except Exception as e:
            return Response({"message": str(e), "success": False})


##### API for fetching several Album ######
class SevaralAlbums(APIView):
    def get(self,request):
        try:
            header=request.headers
            token=header["Authorization"]
            result=several_albums(token)
            # print("====",len(result))
            return Response({"message":"Successful", "success":True, "data":result})
        except Exception as e:
            return Response({"message": str(e), "success": False})


##### API for get album track ######
class AlbumTrack(APIView):
    def get(self,request):
        try:
            header=request.headers
            token=header["Authorization"]
            id=request.GET.get("id")
            type=request.GET.get("album_type")
            limit=request.GET.get("limit")
            offset=request.GET.get("offset")
            result=track_album(token,id,type)
            # print("====",len(result))
            return Response({"message":"Successful", "success":True, "data":result})
        except Exception as e:
            return Response({"message": str(e), "success": False})


##### API for find new releae
class Release(APIView):
    def get(self,request):
        try:
            header=request.headers
            token=header["Authorization"]
            result=new_release(token)
            # print("====",len(result))
            return Response({"message":"Successful", "success":True, "data":result})
        except Exception as e:
            return Response({"message": str(e), "success": False})






