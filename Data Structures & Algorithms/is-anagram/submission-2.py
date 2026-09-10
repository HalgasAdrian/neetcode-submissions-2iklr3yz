class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pointer1 = 0
        pointer2 = 0

        slist = list(s)
        tlist = list(t)

        slist.sort()
        tlist.sort()

        if len(s) != len(t):
            return False
        
        while pointer1 < len(s):
            if slist[pointer1] == tlist[pointer2]:
                pointer1 += 1
                pointer2 += 1
            else:
                return False
        
        return True

        