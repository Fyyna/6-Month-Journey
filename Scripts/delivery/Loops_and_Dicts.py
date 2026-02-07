#temporary dict data for calculations :P no CSV or JSON Parsin yet
delivery_data = [
        {"driver_id": "D1", "pickup_time": "09:00", "dropoff_time": "09:30", "distance_km": 10},
        {"driver_id": "D2", "pickup_time": "09:15", "dropoff_time": "10:00", "distance_km": 20},
        {"driver_id": "D1", "pickup_time": "10:00", "dropoff_time": "10:45", "distance_km": 15},
        {"driver_id": "D3", "pickup_time": "09:30", "dropoff_time": "09:50", "distance_km": 5},
        {"driver_id": "D2", "pickup_time": "10:30", "dropoff_time": "11:30", "distance_km": 25},
    ]

#determines slowest Driver
slowest = None
slowest_driver = None




#function to natively convert HH:MM form a string to an integers in Minutes
def conversion_to_minutes(time_str):

    parts = time_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])

    time = (hours * 60) + minutes

    return time

#Empty Driver Stats dict
driver_stats = {}

#empty slow driver list
slow_deliveries = []

#core Loop
for d in delivery_data:

    #assigns dict entry "driver_id" to variable driver_id to be usable
    driver_id = d["driver_id"]

    #checks if driver id is already in driver_stats dict if it isnt it creates a new entry in the dict with the schematic dict provided
    if driver_id not in driver_stats:
       driver_stats[driver_id] = {
           "total_distance_km": 0,
           "total_time_minutes": 0,
           "total_deliveries": 0
       }

    # extract dict entry for readability and avoiding repeated indexing
    pickup = d["pickup_time"]
    dropoff = d["dropoff_time"]

    #calculates the time it took to deliver with the function conversion_to_minutes using the variables wew created
    delivery_time_minutes = conversion_to_minutes(dropoff) - conversion_to_minutes(pickup)

    #converts the delivery time into hours for speed calculation
    delivery_time_hours = delivery_time_minutes / 60

    #takes the distance we traveled and divides it by time in hours for KM/H
    speed = d["distance_km"] / delivery_time_hours

    #assigns a driver_id to the slow list if it is slower than 20 KM/H
    if speed < 20:
        slow_deliveries.append(d)

        #saves speed to dict entry "speed"
        d["speed"] = speed

        #saves delivery_time_minutes to dict entry "delivery_time_minutes"
        d["delivery_time_minutes"] = delivery_time_minutes


    driver_stats[driver_id]["total_deliveries"] += 1
    driver_stats[driver_id]["total_time_minutes"] += delivery_time_minutes
    driver_stats[driver_id]["total_distance_km"] += d["distance_km"]

    print(f"The delivery took {delivery_time_minutes} minutes and was delivered at an average speed of {speed: .2f} Km/h")

#loop to return Key (driver ID) and values (driver_stats.items()) calculations deliberatly done after we gotten all data to not average averages
for driver_id, stats in driver_stats.items():

    # extract dict entry for readability and avoiding repeated indexing
    total_distance_km = stats["total_distance_km"]

    # extract dict entry for readability and avoiding repeated indexing
    total_time_minutes = stats["total_time_minutes"]

    # extract dict entry for readability and avoiding repeated indexing
    total_deliveries = stats["total_deliveries"]

    #calculates the average distance based on total distance divided by total ammount of deliveries
    average_distance = total_distance_km / total_deliveries

    #calculates average speed based on total distance and minutes / 60 to get KM/H
    average_speed = total_distance_km / (total_time_minutes / 60)


    if slowest is None or average_speed < slowest:
       slowest = average_speed
       slowest_driver = driver_id


    print(f"Driver ID: {driver_id}, Average Distance: {average_distance} km, Average Speed:{average_speed: .2f} KM/H")

print (f"slowest driver was: {slowest_driver} fire this bitch")
