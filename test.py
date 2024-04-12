import pytest
from app import app 
from fastapi.testclient import TestClient 


client = TestClient(app)

def test_department():
    response = client.post("/department/" , json={"name": "RH"})
    assert response.status_code == 201
    assert response.json() == {"name": "RH"}

    response = client.get("/department/")
    assert response.status_code == 200
    assert response.json() == [{"name": "RH"}]
    
def test_employee():
    response = client.post("/employee/", json={"name": "Joao", "department_name": "RH", "dependents": 1})
    response = client.get("/employee/")
    assert response.status_code == 200
    assert response.json() == [{"name": "Joao", "have_dependents": True}]