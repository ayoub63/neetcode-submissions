class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        result = []
        for start, end in intervals:
            
            if result and start <= result[-1][1]:
                curr_end = result[-1][1]
                result[-1][1] = max(end, curr_end)

            else:
                result.append([start, end])

        
        return result