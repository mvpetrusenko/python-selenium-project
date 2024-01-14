import requests
import json
from main import get_spotify_token 



BASE_SPOTIFY_URL = 'https://api.spotify.com'

def create_playlist():
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    } 

    
    url = BASE_SPOTIFY_URL + '/v1/users/smedjan/playlists'
    data = {
        "name": "New Playlist",
        "description": "New playlist description",
        "public": False
    } 
    

    response = requests.post(url, headers=headers, data=json.dumps(data)) 
    print(response.text)
    if response.status_code == 201:
        print("Playlist created successfully!")
    else:
        print(f"Error: {response.status_code}")

    assert response.status_code == 201, "Failed to create playlist"

create_playlist()

    


