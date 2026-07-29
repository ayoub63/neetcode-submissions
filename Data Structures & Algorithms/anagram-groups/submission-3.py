class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []
        freq = defaultdict(list)
        for word in strs:
            counting = [0] * 26
            for c in word:
                
                index = ord(c) - ord("a")
                counting[index] += 1

            freq[tuple(counting)].append(word)  


        return list(freq.values())
