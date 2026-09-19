import urllib.request #import urllib.request module
import urllib.error #import urllib.error module
import json #import json module

BASE_URL = "http://127.0.0.1:8002" #base URL of the server

def get_string():
    print("\n--- GET /string ---")
    try:
        response = urllib.request.urlopen(f"{BASE_URL}/string") #makes the HTTP GET request
        data = response.read().decode() #reads the response data
        print(f"Status: {response.status}") #prints the status code
        print(f"Response: {data}") #prints the response data
        return data
    except urllib.error.URLError as e: #if the request fails
        print(f"Error: {e}") #prints the error
        return None

def get_json():
    print("\n--- GET /json ---")
    try:
        response = urllib.request.urlopen(f"{BASE_URL}/json")
        data = response.read().decode()
        parsed_json = json.loads(data)
        print(f"Status: {response.status}")
        print(f"Response (raw): {data}")
        print(f"Response (parsed): {parsed_json}")
        return parsed_json
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def post_string(message): #POST is sending data to the server
    print(f"\n--- POST /echo-string ---")
    try:
        payload = message.encode() #convert string to bytes for http
        request = urllib.request.Request( #For POST, you need to create a Request object (not just call urlopen directly) because you need to attach data and headers.
            f"{BASE_URL}/echo-string",
            data=payload,
            headers={"Content-Type": "text/plain"}
        )
        response = urllib.request.urlopen(request)
        data = response.read().decode()
        print(f"Status: {response.status}")
        print(f"Response: {data}")
        return data
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def post_json(data_dict):
    print(f"\n--- POST /echo-json ---")
    try:
        payload = json.dumps(data_dict).encode()
        request = urllib.request.Request(
            f"{BASE_URL}/echo-json",
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        response = urllib.request.urlopen(request)
        data = response.read().decode()
        parsed_json = json.loads(data)
        print(f"Status: {response.status}")
        print(f"Response (raw): {data}")
        print(f"Response (parsed): {parsed_json}")
        return parsed_json
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def main():
    print("=" * 60)
    print("Bare-bones HTTP Client")
    print("=" * 60)
    
    get_string()
    get_json()
    post_string("Hello Server!")
    post_json({"name": "Jake", "action": "learning_http"})
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)

# commented out as can only have one per file so incorportaed into function at end of file
# if __name__ == "__main__":
#    main()


#########################################################################################
# Using FAST api instead of barebones: 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ===== FASTAPI CLIENT VERSION =====
FASTAPI_URL = "http://127.0.0.1:8003"

def fastapi_get_string():
    print("\n--- FastAPI GET /string ---")
    try:
        response = urllib.request.urlopen(f"{FASTAPI_URL}/string")
        data = response.read().decode()
        print(f"Status: {response.status}")
        print(f"Response: {data}")
        return data
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def fastapi_get_json():
    print("\n--- FastAPI GET /json ---")
    try:
        response = urllib.request.urlopen(f"{FASTAPI_URL}/json")
        data = response.read().decode()
        parsed_json = json.loads(data)
        print(f"Status: {response.status}")
        print(f"Response (parsed): {parsed_json}")
        return parsed_json
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def fast_api_post_string(message): #POST is sending data to the server
    print(f"\n--- POST /echo-string ---")
    try:
        payload = message.encode() #convert string to bytes for http
        request = urllib.request.Request( #For POST, you need to create a Request object (not just call urlopen directly) because you need to attach data and headers.
            f"{FASTAPI_URL}/echo-string",
            data=payload,
            headers={"Content-Type": "text/plain"}
        )
        response = urllib.request.urlopen(request)
        data = response.read().decode()
        print(f"Status: {response.status}")
        print(f"Response: {data}")
        return data
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def fast_api_post_json(data_dict):
    print(f"\n--- POST /echo-json ---")
    try:
        payload = json.dumps(data_dict).encode()
        request = urllib.request.Request(
            f"{FASTAPI_URL}/echo-json",
            data=payload,
            headers={"Content-Type": "application/json"}
        )
        response = urllib.request.urlopen(request)
        data = response.read().decode()
        parsed_json = json.loads(data)
        print(f"Status: {response.status}")
        print(f"Response (raw): {data}")
        print(f"Response (parsed): {parsed_json}")
        return parsed_json
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def fa_main():
    print("=" * 60)
    print("FASTAPI HTTP Client")
    print("=" * 60)
    
    fastapi_get_string()
    fastapi_get_json()
    fast_api_post_string("Hello Server - fa!")
    fast_api_post_json({"name": "Jake fa", "action": "learning_http fa"})
    
    print("\n" + "=" * 60)
    print("All FA tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    fa_main()