class Solution:
    def isPalindrome(self, s: str) -> bool:
        charlist = [c.lower() for c in s if c.isalnum()]

        left, right = 0, len(charlist) - 1
        while left < right:
            if charlist[left] != charlist[right]:
                return False
            else:
                right -= 1 
                left += 1
        return True
        