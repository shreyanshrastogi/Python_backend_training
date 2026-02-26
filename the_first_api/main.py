from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def status() -> dict[str, str]:
    stat = {"status": "server is running"}

    return stat


@app.get("/profile")
def profile():
    details = {"username": "admin", "role": "python backend developer"}
    return details


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, int | str]:
    id = {"requested_id": user_id, "status": "active"}
    return id


@app.get("/items")
def read_items(skip: int = 0, limit: int = 10) -> dict[str, int]:
    item = {"skip_value": skip, "limit_value": limit}
    return item
