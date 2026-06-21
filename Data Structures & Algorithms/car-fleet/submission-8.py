class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        tuples = []
        for i in range(n):
            tuples.append((position[i], speed[i]))
        tuples.sort(reverse=True)
        processed_cars = 0
        fleets = 0
        curr_time = 0
        for i in range(n):
            time = (target - tuples[i][0]) / tuples[i][1]
            if curr_time is None or time <= curr_time:
                curr_time = max(time, curr_time)
            else:
                fleets += 1
                curr_time = time
        return fleets