from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:  
        self.time_dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_dict.get(key, [])

        l, r = 0, len(values) - 1
        curr = 0
        while l <= r:
            m = (l + r) // 2
            
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1

        
        return res
        
