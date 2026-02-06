
class TravelDistance:

    def __init__(self):
       self._MpS = 6.00

    def travel_time(self):
        travel_time = float(input("Enter the distance in meters: ")) / self._MpS
        return travel_time


#