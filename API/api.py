from main import get_spotify_token
import requests
import json



"""

try:
    BASE_SPOTIFY_URL = 'https://api.spotify.com'

    def check_artist_id(artist_id, expected_id):
        token = get_spotify_token()
        print("Token:", token)  # Print token for debugging
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        print("URL:", BASE_SPOTIFY_URL + str(artist_id))  # Print the formed URL
        response = requests.get(BASE_SPOTIFY_URL + str(artist_id), headers=headers)
        #print("Status code:", response.status_code) 
    #print("Status code:", response.status_code)
        assert response.status_code == 200, "Status code is wrong, expected 200, got {}".format(response.status_code)
        source = json.loads(response.text) 
        actual_id = source['artists'][0]['id']
        assert actual_id == expected_id, "Wrong id, expected {}, got {}".format(expected_id, actual_id)
        print("API response:", source)

except Exception as e:
    print("Exception:", e)


"""    


"""

try: 
    BASE_SPOTIFY_URL = 'https://api.spotify.com'

    def check_artist_id(artist_id, expected_id):
        token = get_spotify_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        response = requests.get(BASE_SPOTIFY_URL + str(artist_id), headers=headers)
        assert response.status_code == 200, "Status code is wrong, expected 200, got {}".format(response.status_code)
        source = json.loads(response.text) 
        #source = json.loads(response.content)
        actual_id = source['artists'][0]['id']
        assert actual_id == expected_id, "Wrong id, expected {}, got {}".format(expected_id, actual_id) 
        #print(source)
        #print(response) 




        # Print the status code and response content for debugging
        print("Status code:", response.status_code)
        #print("Response content:", response.text) 


except Exception as e:
    print("Exception:", e)        


""" 












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
    source = json.loads(response.text) 
    #source = json.loads(response.content)
    actual_id = source['artists'][0]['id']
    assert actual_id == expected_id, "Wrong id, expected {}, got {}".format(expected_id, actual_id) 
    #print(source)
    #print(response) 




    # Print the status code and response content for debugging
    print("Status code:", response.status_code)
    #print("Response content:", response.text) 

    

    
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
    
    source = json.loads(response.content)

    # Print the entire response for inspection
    print("API Response:", source)

    # Assuming 'id' is at the top level of the response
    actual_id = source.get('id', None)

    assert actual_id == expected_id, "Wrong id, expected {}, got {}".format(expected_id, actual_id)

    return source 





