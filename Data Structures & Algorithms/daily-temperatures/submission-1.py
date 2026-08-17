class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                curr_index, curr_temperature = stack.pop()
                difference = index - curr_index
                res[curr_index] = difference

            stack.append((index, temp))

        return res
