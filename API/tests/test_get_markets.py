from API.requests.check_markets import check_markets 
import requests
import json



def test_get_markets():
    endpoint2 = '/v1/markets' 
    expected_market = "QA"
    result = check_markets(endpoint2=endpoint2, expected_market=expected_market)

    print(result)

test_get_markets()