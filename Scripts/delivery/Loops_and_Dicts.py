delivery_data = [
        {"driver_id": "D1", "pickup_time": "09:00", "dropoff_time": "09:30", "distance_km": 10},
        {"driver_id": "D2", "pickup_time": "09:15", "dropoff_time": "10:00", "distance_km": 20},
        {"driver_id": "D1", "pickup_time": "10:00", "dropoff_time": "10:45", "distance_km": 15},
        {"driver_id": "D3", "pickup_time": "09:30", "dropoff_time": "09:50", "distance_km": 5},
        {"driver_id": "D2", "pickup_time": "10:30", "dropoff_time": "11:30", "distance_km": 25},
    ]

slowest = None
slowest_driver = 0





def conversion_to_minutes(time_str):

    parts = time_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])

    time = (hours * 60) + minutes

    return time

driver_stats = {}


#print (conversion_to_minutes(delivery_data[0]["pickup_time"]))

slow_deliveries = []
for d in delivery_data:

    driver_id = d["driver_id"]
    if driver_id not in driver_stats:
       driver_stats[driver_id] = {
           "total_distance_km": 0,
           "total_time_minutes": 0,
           "total_deliveries": 0
       }



    pickup = d["pickup_time"]
    dropoff = d["dropoff_time"]
    delivery_time_minutes = conversion_to_minutes(dropoff) - conversion_to_minutes(pickup)
    delivery_time_hours = delivery_time_minutes / 60
    speed = d["distance_km"] / delivery_time_hours

    if speed < 20:
        slow_deliveries.append(d)
        d["speed"] = speed
        d["delivery_time_minutes"] = delivery_time_minutes


    driver_stats[driver_id]["total_deliveries"] += 1
    driver_stats[driver_id]["total_time_minutes"] += delivery_time_minutes
    driver_stats[driver_id]["total_distance_km"] += d["distance_km"]

    print(f"The delivery took {delivery_time_minutes} minutes and was delivered at an average speed of {speed: .2f} Km/h")


for driver_id, stats in driver_stats.items():

   total_distance_km = stats["total_distance_km"]

   total_time_minutes = stats["total_time_minutes"]

   total_deliveries = stats["total_deliveries"]

   average_distance = total_distance_km / total_deliveries

   average_speed = total_distance_km / (total_time_minutes / 60)

   if slowest is None or average_speed < slowest:
       slowest = average_speed
       slowest_driver = driver_id


   print(f"Driver ID: {driver_id}, Average Distance: {average_distance}, Average Speed:{average_speed: .2f}")



print (f"slowest driver was: {slowest_driver} fire this bitch")
