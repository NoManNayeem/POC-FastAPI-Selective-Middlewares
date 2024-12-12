import httpx

BASE_URL = "http://127.0.0.1:8000"

def test_routes():
    test_cases = [
        {"method": "GET", "url": "/without-middleware", "expected_message": "This route does not use middleware."},
        {"method": "POST", "url": "/without-middleware", "expected_message": "This POST route does not use middleware."},
        {"method": "GET", "url": "/with-middleware", "expected_message": "This route uses middleware."},
        {"method": "POST", "url": "/with-middleware", "expected_message": "POST request with middleware."},
    ]

    for case in test_cases:
        method = case["method"].lower()
        url = f"{BASE_URL}{case['url']}"
        print(f"Testing {case['method']} {case['url']}")

        if method == "get":
            response = httpx.get(url)
        elif method == "post":
            response = httpx.post(url)
        
        assert response.status_code == 200, f"Failed {case['method']} {case['url']}"
        assert response.json()["message"] == case["expected_message"], f"Unexpected response for {case['method']} {case['url']}"
        print(f"Test passed for {case['method']} {case['url']}")

if __name__ == "__main__":
    test_routes()
    print("All tests passed!")
