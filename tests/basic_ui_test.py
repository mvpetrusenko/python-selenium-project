from selenium import webdriver 
from selenium.webdriver.common.by import By 
import pytest 



@pytest.fixture()  


def browser(): 
    path_to_chrome_driver = 'C:\\chromedriver-win64'
    chrome_browser = webdriver.Chrome(path_to_chrome_driver) 
    chrome_browser.implicitly_wait(10) 
    return chrome_browser 


def test_button_create_playlist_exist(browser): 
    browser.get('https://open.spotify.com/') 
    assert browser.find_element(By.XPATH, '//button[@data-encore-id="buttonPrimary"]').is_displayed()
