from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main_route():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"mensaje": "Hola mundo"}

def test_endpoint_datos_invalidos():
  response = client.get("/evaluar/tarjetas?edad=-34&ingresos=-94")
  assert response.status_code == 400
  assert response.json()["detail"] == "Datos inválidos"

def test_endpoint_rechazo():
  response = client.get("/evaluar/tarjetas?edad=17&ingresos=2000")
  assert response.status_code == 200
  assert response.json()["status"] == "RECHAZADO"

def test_endpoint_regular():
  response = client.get("/evaluar/tarjetas?edad=21&ingresos=2000")
  assert response.status_code == 200
  assert response.json()["status"] == "APRO"
