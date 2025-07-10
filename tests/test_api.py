from app.api import app

def test_success():
    client = app.test_client() #Crea un cliente de pruebas de Flask sin necesidad de que el servidor esté realmente corriendo
    res = client.post("/price", json = {"price": 990, "coupon": "SALE10"})
    assert res.status_code == 200
    
#forzamos el fallo para saber si la anterior es valida
def test_failure():
    client = app.test_client()
    res = client.post("/price", json = {"price": "990", "coupon": "SALE10"})
    assert res.status_code == 500