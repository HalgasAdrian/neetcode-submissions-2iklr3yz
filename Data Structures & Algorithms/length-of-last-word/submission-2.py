class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Iterate from the end of the array to find the first word

        Make sure to skip over any trailing spaces until we hit the word
        count each character, stop once we hit another ' '.
        """
        count = 0
        end = len(s) - 1 
        pointer = end

        while pointer >= 0:
            if s[pointer] == ' ':
                pointer -= 1
            else:
                break
        
        while pointer >= 0 and s[pointer] != ' ':
            count += 1
            pointer -= 1
        
        return count
        