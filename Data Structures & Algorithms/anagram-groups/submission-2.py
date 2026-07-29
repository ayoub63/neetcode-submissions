class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counting = [0] * 26
        res = []
        freq = defaultdict(list)
        for word in strs:
            for c in word:
                index = ord(c) - ord("a")
                counting[index] += 1

            freq[tuple(counting)].append(word)  

        for lists in freq.values():
            res.append(lists)

        return res
