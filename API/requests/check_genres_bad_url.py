from main import get_spotify_token
import requests
import json


    

BASE_SPOTIFY_URL = 'https://api.spotify.com'

def check_genres(endpoint3, expected_genre3):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.get(BASE_SPOTIFY_URL + str(endpoint3), headers=headers)
    assert response.status_code == 404, "Status code is wrong, expected 404, got {}".format(response.status_code)
    
    source = json.loads(response.content)


    print("API Response:", source)

    actual_genres = source.get('genres', None)

    #assert actual_genres == expected_genre, "Wrong genres, expected {}, got {}".format(expected_genre, actual_genres)

    assert expected_genre3 in actual_genres, "Expected genre not found, expected {}, got {}".format(expected_genre3, actual_genres3)

    
    return source