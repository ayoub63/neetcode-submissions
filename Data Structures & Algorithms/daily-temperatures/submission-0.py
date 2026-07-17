class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                indexcur, tempcur = stack.pop()
                difference = index - indexcur
                result[indexcur] = difference

            stack.append([index, temp])

        return result

        