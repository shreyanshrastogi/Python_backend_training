from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

book = {}


class Room(BaseModel):
    room_type: str
    price: float
    is_available: bool


@app.get("/rooms")
def list_rooms():
    return book


@app.get("/rooms/available")
def room_available():
    available = {}
    for room_id, room in book.items():
        if room.is_available:
            available[room_id] = room

    return available


@app.get("/rooms/{room_id}")
def check_room(room_id: int):
    if room_id not in book:
        raise HTTPException(status_code=404, detail="room not found")
    return book[room_id]


@app.post("/rooms/add/{room_id}")
def add_room(room_id: int, room_data: Room):
    if room_id in book:
        raise HTTPException(status_code=409, detail="room already in book")
    book[room_id] = room_data
    return {"message": "room added successfully", "room data": room_data}


@app.put("/rooms/book/{room_id}")
def book_room(room_id: int):
    if room_id not in book:
        raise HTTPException(status_code=404, detail="room not available in book")
    if not book[room_id].is_available:
        raise HTTPException(status_code=400, detail="room is not available")

    book[room_id].is_available = False
    return {"message": "room booked successfully", "room_id": room_id}


@app.put("/rooms/checkout/{room_id}")
def checkout_room(room_id: int):
    if room_id not in book:
        raise HTTPException(status_code=404, detail="room not found")
    if book[room_id].is_available:
        raise HTTPException(status_code=400, detail="room already available")
    book[room_id].is_available = True
    return {"message": "room checked out", "room_id": room_id}


@app.delete("/rooms/remove/{room_id}")
def delete_room(room_id: int):
    if room_id not in book:
        raise HTTPException(status_code=404, detail="room already not in book")
    del book[room_id]
    return {"message": "room deleted successfully"}
