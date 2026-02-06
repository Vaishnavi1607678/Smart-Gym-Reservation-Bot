from fastapi import FastAPI
from backend.model import predict_least_crowded
from backend.database import conn
from backend.notifier import send_notification

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Smart Gym Bot Running"}

@app.get("/recommend")
def recommend():
    return predict_least_crowded()

@app.post("/book")
def book_slot(name: str, hour: int):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO bookings (name, hour) VALUES (?, ?)",
        (name, hour)
    )
    conn.commit()

    send_notification(name, hour)

    return {
        "message": "Slot booked successfully",
        "name": name,
        "hour": hour
    }

