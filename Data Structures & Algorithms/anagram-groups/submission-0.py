class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        
        for word in strs:
            frequency_arr = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                frequency_arr[index] += 1
        
            
            key = tuple(frequency_arr)

            if key not in groups.keys():
               groups[key] = []

            
            groups[key].append(word)


        return list(groups.values())    