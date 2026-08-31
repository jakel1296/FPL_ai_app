from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def healthcheck():
    return {"message": "Backend alive"}
