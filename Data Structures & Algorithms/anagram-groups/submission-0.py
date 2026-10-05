class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_dict = {}

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in anagram_dict:
                anagram_dict[key] = []

            anagram_dict[key].append(strs[i])

        for key in anagram_dict:
            result.append(anagram_dict[key])
    
        return result