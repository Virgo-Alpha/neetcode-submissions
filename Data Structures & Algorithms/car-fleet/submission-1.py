class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Without using a stack
        number_of_fleets = 0
        last_fleet_time = 0
        for pos, spd in sorted(zip(position, speed), reverse=True):
            time_taken = (target-pos) / spd
            if time_taken > last_fleet_time:
                last_fleet_time = time_taken
                number_of_fleets += 1
        return number_of_fleets
