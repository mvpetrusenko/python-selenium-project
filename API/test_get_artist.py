"""


from api import check_artist_id 


def test_check_artist_id():
    artist_id = '/v1/artists/2CIMQHirSU0MQqyYHq0eOx'
    check_artist_id(artist_id=artist_id, expected_id="2CIMQHirSU0MQqyYHq0eOx") 




"""    


from api import check_artist_id  

#from main import check_artist_id, get_spotify_token
import requests
import json



def test_check_artist_id():
    artist_id = '/v1/artists/2CIMQHirSU0MQqyYHq0eOx'
    result = check_artist_id(artist_id=artist_id, expected_id="2CIMQHirSU0MQqyYHq0eOx")

    # Print the result
    print(result)

# Call the test function
test_check_artist_id()