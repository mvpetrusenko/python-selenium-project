from main import get_spotify_token
import requests
import json


    

BASE_SPOTIFY_URL = 'https://api.spotify.com'

def check_markets(endpoint2, expected_market):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.get(BASE_SPOTIFY_URL + str(endpoint2), headers=headers)
    assert response.status_code == 200, "Status code is wrong, expected 200, got {}".format(response.status_code)
    
    source = json.loads(response.content)


    print("API Response:", source)

    # Check if 'markets' key is present in the response
    actual_markets = source.get('markets')
    if actual_markets is None:
        assert False, "No 'markets' key found in the response"

    # Check if expected_market is in actual_markets
    assert expected_market in actual_markets, "Expected market not found, expected {}, got {}".format(expected_market, actual_markets)

    return source



