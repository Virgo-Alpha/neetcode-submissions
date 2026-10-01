class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We use a stack and pop each fleet_times as we add it to the fleet_timess
        fleet_times = []

        # speed = d / t
        #  The d in our case is max capped at target
        # remaining_distance = target - position[i]
        # Time to cover remaining distance = remaining_distance / speed
        # This is the same as time = (target - position[i]) / speed[i]

        # Array of cars and their speeds sorted in descending order by position:
        #   = [position][speed]

        car_speed = list(zip(position, speed))

        # ! Sort by position but in descending order
        car_speed.sort(key=lambda x: -x[0]) # logn time complexity (timsort, I think)

        for pair in car_speed:
            time = (target - pair[0]) / pair[1]

            if not fleet_times or time > fleet_times[-1]:
                fleet_times.append(time)

        return len(fleet_times)
