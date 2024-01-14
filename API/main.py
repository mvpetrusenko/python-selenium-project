import base64
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

def get_spotify_token():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        token = response.json()["access_token"]
        return token
    else:
        raise Exception("Failed to get access token from Spotify API") 
    

token = get_spotify_token()
print(token) 







"""


BASE_SPOTIFY_URL = 'https://api.spotify.com'

def check_artist_id(artist_id, expected_id):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.get(BASE_SPOTIFY_URL + str(artist_id), headers=headers)
    assert response.status_code == 200, "Status code is wrong, expected 200, got {}".format(response.status_code)
    #source = json.loads(response.text) 
    source = json.loads(response.content)
    #actual_id = source['artists'][0]['id']
    assert actual_id == expected_id, "Wrong id, expected {}, got {}".format(expected_id, actual_id) 
    #print(source)
    #print(response) 


    return source  


def test_check_artist_id():
    artist_id = '/v1/artists/2CIMQHirSU0MQqyYHq0eOx'
    check_artist_id(artist_id=artist_id, expected_id="2CIMQHirSU0MQqyYHq0eOx")

source = check_artist_id 
print(source)


    #rsc =  response.status_code 
    #return rsc  
    #print(response.status_code) 

    # Print the status code and response content for debugging
    #print("Status code:", response.status_code)
    #print("Response content:", response.text)  

#sc = check_artist_id 
#print(sc) 



""" 




""" OK code


BASE_SPOTIFY_URL = 'https://api.spotify.com'

def check_artist_id(artist_id, expected_id):
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    response = requests.get(BASE_SPOTIFY_URL + str(artist_id), headers=headers)
    assert response.status_code == 200, "Status code is wrong, expected 200, got {}".format(response.status_code)
    
    source = json.loads(response.content)

    # Print the entire response for inspection
    print("API Response:", source)

    # Assuming 'id' is at the top level of the response
    actual_id = source.get('id', None)

    assert actual_id == expected_id, "Wrong id, expected {}, got {}".format(expected_id, actual_id)

    return source  

def test_check_artist_id():
    artist_id = '/v1/artists/2CIMQHirSU0MQqyYHq0eOx'
    result = check_artist_id(artist_id=artist_id, expected_id="2CIMQHirSU0MQqyYHq0eOx")

    # Print the result
    print(result)

# Call the test function
test_check_artist_id() 




"""
