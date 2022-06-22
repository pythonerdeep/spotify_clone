from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .spotify_script import *



# Create your views here.

#### API for find albums from spotify and inserting into db"
class Album(APIView):
    def get(self,request):
        try:
            header=request.headers
            token=header["Authorization"]
            album_id=request.GET.get("id")
            result=find_album(token,album_id)
            print(result)
            return Response({"message":"Successful", "success":True,})
        except Exception as e:
            return Response({"message": str(e), "success": False})






