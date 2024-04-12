from fastapi import testclient

from app import app

client_test = testclient.TestClient(app)


def test_post_departament():
    response = client_test.post("/department/", json={"name": "TI"})
    assert response.status_code == 201
    assert response.json() == {"name": "TI"}
    
    response = client_test.post("/department/", json={"name": "RH"})
    assert response.status_code == 201
    assert response.json() == {"name": "RH"}
    
    response = client_test.post("/department/", json={"name": "Vendas"})
    assert response.status_code == 201
    assert response.json() == {"name": "Vendas"}

def test_get_departament():
    
    response = client_test.get("/department/")
    assert response.status_code == 200
    assert response.json() == {"departments": [{"name": "TI"}, {"name": "RH"}, {"name": "Vendas"}]}
    
    
