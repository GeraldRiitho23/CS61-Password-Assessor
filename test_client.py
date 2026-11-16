import requests
import time

url = "http://localhost:5001/assess"

def test_password(password):
    payload = {"password": password}
    print(f"Sending: {payload}")
    
    start_time = time.time()
    response = requests.post(url, json=payload)
    end_time = time.time()
    
    if response.status_code == 200:
        print(f"Received: {response.json()}")
        print(f"Response time: {(end_time - start_time) * 1000:.2f} milliseconds")
    else:
        print(f"Error {response.status_code}: {response.json()}")
    print("-" * 50)

# Test 1: Weak (Fails length and symbol)
print("--- TEST 1: Weak Password ---")
test_password("pass123")

# Test 2: Strong (Passes all rules)
print("--- TEST 2: Strong Password ---")
test_password("P@ssw0rd2023")

# Test 3: Compromised
print("--- TEST 3: Compromised Password ---")
test_password("password123")

# Test 4: Specific Rubric Check (Must return Weak)
print("--- TEST 4: Rubric Check ('123456') ---")
test_password("123456")
