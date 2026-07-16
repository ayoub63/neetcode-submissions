class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1


        buckets = [[] for _ in range(len(nums) + 1)]
        result = []


        for n , f in frequency.items():
            buckets[f].append(n)


        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                   return result 
