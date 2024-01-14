from main import get_spotify_token
import requests
import json


    

BASE_SPOTIFY_URL = 'https://api.spotify.com'

def check_negative_artist_id(artist_id2, expected_id):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.get(BASE_SPOTIFY_URL + str(artist_id2), headers=headers)
    assert response.status_code == 200, "Status code is wrong, expected 200, got {}".format(response.status_code)
    
    source = json.loads(response.content)


    print("API Response:", source)

    actual_id2 = source.get('id', None)

    assert actual_id2 == expected_id, "Wrong id, expected {}, got {}".format(expected_id, actual_id2)

    return source 





