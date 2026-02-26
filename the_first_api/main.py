from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def status() -> dict[str, str]:
    stat = {"status": "server is running"}

    return stat


@app.get("/prof")
def profile():
    details = {"username": "admin", "role": "python backend developer"}
    return details
