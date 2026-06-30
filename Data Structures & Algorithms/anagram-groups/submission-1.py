from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        size_arr = [0] * 26
        anagrams = defaultdict(list)


        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)
            

            anagrams[key].append(s)

        return list(anagrams.values())   