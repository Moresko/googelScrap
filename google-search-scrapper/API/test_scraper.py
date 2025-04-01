import pytest
from fastapi.testclient import TestClient
from .scraper import app  
import requests

client = TestClient(app)

def test_value_false():
    response = client.post("/string", json={"notValue": "test"})
    assert response.status_code == 422  

def test_value_true():
    response = client.post("/string", json={"value": "test"})
    assert response.status_code == 200 

def test_long_word():
    word = "ab" * 100
    response = client.post("/string", json={"value": word})
    assert response.status_code == 200

def test_small_word():
    word = "a"
    response = client.post("/string", json={"value": word})
    assert response.status_code == 200

def test_wrong_password():
    url = 'https://realtime.oxylabs.io/v1/queries'
    auth = ('Martin_1AbZT', 'hello')  
    response = requests.post(url, auth=auth)  
    assert response.status_code == 401

def test_wrong_name():
    url = 'https://realtime.oxylabs.io/v1/queries'
    auth = ('hello', 'xydWox_1pedpi_jufsab')  
    response = requests.post(url, auth=auth)  
    assert response.status_code == 401

def test_web_scrapper_file():
    response = client.post("/string", json={"value": "hello"})  

    assert response.status_code == 200  

    assert response.headers["Content-Type"].startswith("text/csv")

    assert "Content-Disposition" in response.headers
    assert "attachment; filename=" in response.headers["Content-Disposition"]

    csv_content = response.content.decode("utf-8") 
    assert csv_content.strip() != ""  



