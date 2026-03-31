class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Is s1 always smaller than s2?
        """
        if s1 == s2:
            return True
        
        l = 0
        r = 0

        letterbank = list(s1)
        long = list(s2)

        while r < len(s2):
            if long[r] in letterbank:
                target = long[r]
                letterbank.remove(target)
                r += 1
                if len(letterbank) == 0:
                    return True
            else:
                # If the character is in s1 but we used up its count, 
                # we need to slide the left pointer and return characters to the bank
                if long[r] in s1:
                    letterbank.append(long[l])
                    l += 1
                else:
                    l = r + 1
                    r = l
                    letterbank = list(s1)

        return False
