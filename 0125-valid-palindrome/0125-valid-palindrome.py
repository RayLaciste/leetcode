class Solution:
    def isPalindrome(self, string: str) -> bool:
        # isalnum
        my_string = ''

        for s in string:
            if s.isalnum():
                my_string += s.lower()
        
        print(my_string)
        l, r = 0, len(my_string) - 1
        
        while l <= r:
            if my_string[l] == my_string[r]:
                l += 1
                r -= 1
            else:
                return False

        return True