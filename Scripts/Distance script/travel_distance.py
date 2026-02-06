#small travel calculator to learn practical use of /
# D = Distance DS = Distance per Second
import distance_calculation

distance = distance_calculation.TravelDistance()
calc = distance.travel_time()


print (f"The trip will take {calc} second")