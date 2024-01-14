from API.requests.check_genres import check_genres 
import requests
import json



def test_get_genres():
    endpoint = '/v1/recommendations/available-genre-seeds' 
    expected_genre = "piano"
    result = check_genres(endpoint=endpoint, expected_genre=expected_genre)

    print(result)

test_get_genres()