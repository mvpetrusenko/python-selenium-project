from API.requests.check_genres_bad_url import check_genres_bad_url
import requests
import json



def test_get_genres_bad_url():
    endpoint3 = '/v1/recommendations/available-genre-seeds@' 
    expected_genre3 = "piano"
    result3 = check_genres_bad_url(endpoint3=endpoint3, expected_genre3=expected_genre3)

    print(result3)

test_get_genres_bad_url()