#Wingin this :P
#taskk: You work for a small delivery company. Every day, drivers complete deliveries across the city. The company wants to analyze driver efficiency and identify delays.
#You’re given a list of deliveries for one day. Each delivery includes:
#driver_id
#pickup_time
#dropoff_time
d#istance_km
#Your task is to write a Python program that analyzes this data.
#Input Data (Example)
#deliveries = [
 #   {"driver_id": "D1", "pickup_time": "09:00", "dropoff_time": "09:30", "distance_km": 10},
  #  {"driver_id": "D2", "pickup_time": "09:15", "dropoff_time": "10:00", "distance_km": 20},
   # {"driver_id": "D1", "pickup_time": "10:00", "dropoff_time": "10:45", "distance_km": 15},
#   {"driver_id": "D3", "pickup_time": "09:30", "dropoff_time": "09:50", "distance_km": 5},
    #{"driver_id": "D2", "pickup_time": "10:30", "dropoff_time": "11:30", "distance_km": 25},
#]
#Your Tasks
#Write Python code to:
#Calculate delivery duration (in minutes) for each delivery
#Compute average speed for each delivery (km/h)
#Flag slow deliveries
#A delivery is considered slow if average speed < 20 km/h
#Summarize per driver:
#Total distance driven
#Total time spent delivering
#Average speed across all deliveries
#Identify the slowest driver (lowest average speed)
#Expected Output (Conceptual)
#Driver D1:
 # Total Distance: 25 km
  #Total Time: 75 minutes
  #Average Speed: 20 km/h

#Driver D2:
 # Total Distance: 45 km
  #Total Time: 105 minutes
  #Average Speed: 25.7 km/h

#Driver D3:
 # Total Distance: 5 km
  #Total Time: 20 minutes
  #Average Speed: 15 km/h

#Slow Deliveries:
#Driver D3 at 15 km/h,

#Slowest Driver of the Day: D3

from datetime import datetime







delivery_data = [
        {"driver_id": "D1", "pickup_time": "09:00", "dropoff_time": "09:30", "distance_km": 10},
        {"driver_id": "D2", "pickup_time": "09:15", "dropoff_time": "10:00", "distance_km": 20},
        {"driver_id": "D1", "pickup_time": "10:00", "dropoff_time": "10:45", "distance_km": 15},
        {"driver_id": "D3", "pickup_time": "09:30", "dropoff_time": "09:50", "distance_km": 5},
        {"driver_id": "D2", "pickup_time": "10:30", "dropoff_time": "11:30", "distance_km": 25},
    ]

def to_minutes(hhmm: str) -> int:
    dt = datetime.strptime(hhmm, "%H:%M")
    return dt.hour * 60 + dt.minute



def analyze_driver (delivery_data):
    delivery_times = []



    for d in delivery_data:
        delivery_time = to_minutes(d["dropoff_time"] - d["pickup_time"])
        delivery_times.append(delivery_time)
        print (delivery_time)





    analyzed_data = {
        "driver_id": delivery_data["driver_id"],
        "delivery_time": "0",
        "speed": "0",
        "distance_km": "0",
        "slow": "0"
    }