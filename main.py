from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Jenkins Pipeline + FastAPI"}

@app.get("/name/")
def name():
    return "my self jenkins deployer"
