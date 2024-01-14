from API.requests.check_artist_id import check_artist_id  
import requests
import json



def test_check_artist_id():
    artist_id = '/v1/artists/2CIMQHirSU0MQqyYHq0eOx' 
    
    result = check_artist_id(artist_id=artist_id, expected_id="2CIMQHirSU0MQqyYHq0eOx")

    print(result)

test_check_artist_id()