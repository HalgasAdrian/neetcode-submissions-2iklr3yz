class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        pointer = len(s) - 1

        # Phase 1: Skip trailing spaces
        while pointer >= 0 and s[pointer] == ' ':
            pointer -= 1
        
        # Phase 2: Count characters until the next space (or start of string)
        while pointer >= 0 and s[pointer] != ' ':
            ans += 1
            pointer -= 1
            
        return ans