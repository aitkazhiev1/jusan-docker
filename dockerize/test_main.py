import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sum1n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

def test_fibo():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_reverse():
    headers = {"string": "hello"}
    response = client.post("/reverse", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

def test_add_to_list():
    element = {"element": "Apple"}
    response = client.put("/list", json=element)
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

def test_get_list():
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

def test_calculator():
    expression = {"expr": "1,+,1"}
    response = client.post("/calculator", json=expression)
    assert response.status_code == 400
    assert response.json() == {"result": 2}
