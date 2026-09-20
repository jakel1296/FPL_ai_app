import urllib.request #import urllib.request module
import urllib.error #import urllib.error module
import json #import json module

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FPL_BS_URL = "https://fantasy.premierleague.com/api/bootstrap-static/" 

def fetch_fpl_data():
    try:
        response = urllib.request.urlopen(FPL_BS_URL)
        data = response.read().decode()
        parsed_json = json.loads(data)
        return parsed_json
    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

@app.get("/json")
def fastapi_get_json():
    fpl_data = fetch_fpl_data()
    if fpl_data is None:
        return {"error": "Failed to fetch FPL data"}
    else:
        second_names = []
        xg = []
        for player in fpl_data["elements"]:
            second_names.append(player["second_name"])
            xg.append(player["expected_goals"])
        return {
            "second_names": second_names,
            "xg": xg
        }

    
@app.get("/hello")
def healthcheck():
    return {"message": "Backend alive"}



