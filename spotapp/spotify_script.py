import json
from tkinter import S
import requests


##### global variable decaler here ####
SPOTIFY_URL="https://api.spotify.com/v1/"
# ACCESS_TOKEN=""

### function for several albums
def several_albums():
    ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
    response=requests.get(
        SPOTIFY_URL+"albums/?"+"ids="+ids
    )
    json_res=response.json()
    return json_res


#### function for fetching albums
def find_album(token,id):
    # print(SPOTIFY_URL+"albums/"+id)
    response=requests.get(
        SPOTIFY_URL+"albums/"+id,
        headers={
            "Authorization":token
        }
    )
    json_res=response.json()
    return json_res


#### function for tracking album
def track_album(token,id,track_type):
    response=requests.get(
        SPOTIFY_URL+"albums/"+id+"/"+track_type,
        headers={
            "Authorization":token
        }
    )
    json_res=response.json()
    return json_res

#### function to browse new_release album
def new_release(token):
    response=requests.get(
        SPOTIFY_URL+"browse/new-releases",
        headers={
            "Authorization":token
        }
    )
    json_res=response.json()
    return json_res

#### delete album function

def remove_album(token,id):
    response=requests.get(
        SPOTIFY_URL+"me/albums?"+id,
        headers={
            "Authorization":token
        }
    )
    json_res=response.json()
    if json_res["error"]=="error":
        return json_res
    else:
        return json_res
