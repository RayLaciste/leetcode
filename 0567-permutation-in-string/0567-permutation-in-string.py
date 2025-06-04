class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): # corner case
            return False

        l, r = 0, len(s1) # static window
        
        while r<=len(s2):
            if sorted(s1) == sorted(s2[l:r]):
                return True
            l+=1
            r+=1
            
        return False