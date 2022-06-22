import json
import requests


# ##### global variable decaler here ####
# SPOTIFY_URL="https://api.spotify.com/v1/"
# # ACCESS_TOKEN=""

# ### function for several albums
# def several_albums():
#     ids="382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"
#     response=requests.get(
#         SPOTIFY_URL+"albums/?"+"ids="+ids
#     )
#     json_res=response.json()
#     return json_res


# #### function for fetching albums
# def find_album(token,id):
#     # print(SPOTIFY_URL+"albums/"+id)
#     response=requests.get(
#         SPOTIFY_URL+"albums/"+id,
#         headers={
#             "Authorization":token
#         }
#     )
#     json_res=response.json()
#     return json_res


# #### function for tracking album
# def track_album(token,id,track_type):
#     response=requests.get(
#         SPOTIFY_URL+"albums/"+id+"/"+track_type,
#         headers={
#             "Authorization":token
#         }
#     )
#     json_res=response.json()
#     return json_res

# #### function to browse new_release album
# def new_release(token):
#     response=requests.get(
#         SPOTIFY_URL+"browse/new-releases",
#         headers={
#             "Authorization":token
#         }
#     )
#     json_res=response.json()
#     return json_res

# #### delete album function

# def remove_album(token,id):
#     response=requests.get(
#         SPOTIFY_URL+"me/albums?"+id,
#         headers={
#             "Authorization":token
#         }
#     )
#     json_res=response.json()
#     if json_res["error"]=="error":
#         return json_res
#     else:
#         return json_res


URL= "https://api.spotify.com/v1/"
def find_album(token, id):
    response=requests.get(url=URL+"albums/"+id,
                        headers={
                        "Authorization":token
                        }
                    )
    json_resp=response.json()
    # print(json_resp)
    # if json_resp['error']=='error':
    #     return {'message':json_resp['error']['message'], 'success':False}

    album={
        'album_id':json_resp['id'],
        'album_name':json_resp['name'],
        'album_url':json_resp['href'],
        'label':json_resp['label'],
        'release_date':json_resp['release_date'],
        'total_tracks':json_resp['total_tracks'],
        'album_type':json_resp['album_type'],
        'artists':json_resp['artists'][0]['name'],        
    }

    tracks=[]
    all_tracks=json_resp['tracks']['items']
    for track in all_tracks:
        track_dict={}
        track_dict['album_id']=json_resp['id']
        track_dict['track_id']=track['id']
        track_dict['track_name']=track['name']
        track_dict['duration']=track['duration_ms']
        track_dict['artist']=track['artists'][0]['name']
        track_dict['url']=track['href']

        tracks.append(track_dict)

    # print(album)
    # print(tracks)
    return {
        'album':album,
        'tracks':tracks
        }
# find_album("29njH6pDF6JE65D2VJbAxW")


# def get_newrelease():
#     response=requests.get(url=URL+"browse/new-releases",
#                         headers={
#                         "Authorization":ACCESS_TOKEN
#                         }
#                             )

#     json_resp=response.json()
#     print(json_resp)
# get_newrelease()
