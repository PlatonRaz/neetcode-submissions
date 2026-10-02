class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        
        if len(s) != len(t):
            return False

        for letter in s:
            mapS[letter] = mapS.get(letter, 0) + 1
    
        for letter in t:
            if letter not in mapS:
                return False

            mapS[letter] -= 1
            
            if mapS[letter] < 0:
                return False
      
        return True


        