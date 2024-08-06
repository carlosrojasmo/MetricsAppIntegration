from src.app import app

def test_metrics():
    with app.test_client() as c:
        response = c.get('/metrics')
        assert response.status_code == 200
        #assert b"cpu_usage_percent" in response.data

test_metrics