class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = set()
        l,res = 0,0
        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l+=1
            string.add(s[r])
            res = max(res, len(string))
        return res