class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        How many characters from t are missing in s?

        Using a two pointer approach, one for each string

        We compare s and t to see if we have a match
        if we match, move both pointers forward
        """
        pointer1 = 0
        pointer2 = 0

        while pointer1 < len(s) and pointer2 < len(t):
            if s[pointer1] == t[pointer2]:
                pointer1 += 1
                pointer2 += 1
            elif s[pointer1] != t[pointer2]:
                pointer1 += 1
        return len(t) - pointer2 

        
        