

class PetroPump:
    def __init__(self, petrol, distance):
        self.petrol = petrol
        self.distance = distance


def truck_tour():
    stops = int(input())
    tank = []
    for stop in range(stops):
        if 1 <= stops <= 1000001:
            petrol, distance = [int(el) for el in input().split() if 1 <= int(el) <= 1000000000]
            tank.append(PetroPump(petrol, distance))
    start = 0
    stop_pos = 1
    current_fuel = tank[start].petrol - tank[start].distance
    while start != stop_pos or current_fuel < 0:
        while start != stop_pos and current_fuel < 0:
            current_fuel -= tank[start].petrol - tank[start].distance
            start = (start + 1) % stops
            if start == 0:
                break

        current_fuel += tank[stop_pos].petrol - tank[stop_pos].distance
        stop_pos = (stop_pos + 1) % stops
    print(start)


truck_tour()
