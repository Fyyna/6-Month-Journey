#Wingin this :P
from datetime import datetime


def to_minutes(hhmm: str) -> int:
    dt = datetime.strptime(hhmm, "%H:%M")
    return dt.hour * 60 + dt.minute




deliveries = [
    {"driver_id": "D1", "pickup_time": "09:00", "dropoff_time": "09:30", "distance_km": 10},
    {"driver_id": "D2", "pickup_time": "09:15", "dropoff_time": "10:00", "distance_km": 20},
    {"driver_id": "D1", "pickup_time": "10:00", "dropoff_time": "10:45", "distance_km": 15},
    {"driver_id": "D3", "pickup_time": "09:30", "dropoff_time": "09:50", "distance_km": 5},
    {"driver_id": "D2", "pickup_time": "10:30", "dropoff_time": "11:30", "distance_km": 25},
]