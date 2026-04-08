from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_version():
    client = app.test_client()
    response = client.get("/version")
    assert response.status_code == 200
    data = response.get_json()
    assert data["version"] == "1.0.0"


def test_get_shipments():
    client = app.test_client()
    response = client.get("/api/shipments")
    assert response.status_code == 200
    data = response.get_json()
    assert "shipments" in data


def test_get_single_shipment():
    client = app.test_client()
    response = client.get("/api/shipments/IA1001")
    assert response.status_code == 200


def test_missing_shipment():
    client = app.test_client()
    response = client.get("/api/shipments/UNKNOWN")
    assert response.status_code == 404