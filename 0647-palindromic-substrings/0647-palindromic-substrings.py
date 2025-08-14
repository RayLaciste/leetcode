class Solution:
    def countSubstrings(self, s: str) -> int:
        substrings = []
        total = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substrings.append(s[i:j])
    
        for ss in substrings:
            if ss == ss[::-1]:
                total += 1
                
        return total