class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        parking_temperatures = []

        for index, temp in enumerate(temperatures):
            while parking_temperatures and temp > parking_temperatures[-1][1]:
                parked_index, parked_temp = parking_temperatures.pop()
                day_difference = index - parked_index
                result[parked_index] = day_difference

            parking_temperatures.append((index, temp))
        
        return result