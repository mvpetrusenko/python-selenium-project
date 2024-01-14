from API.requests.check_negative_artist_id import check_negative_artist_id 
import requests
import json



def test_check_artist_id():
    
    artist_id2 = '/v1/artists/1111111111'
    result = check_negative_artist_id(artist_id2=artist_id2, expected_id="2CIMQHirSU0MQqyYHq0eOx")

    print(result)

test_check_artist_id()