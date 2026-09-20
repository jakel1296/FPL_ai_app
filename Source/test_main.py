from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

#def test_a():
#    response = client.get("/a")
#    assert response.status_code == 200

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
