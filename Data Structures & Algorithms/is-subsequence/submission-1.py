class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sPoint = 0
        tPoint = 0

        if s == t:
            return True

        while tPoint < len(t) and sPoint < len(s):
            if s[sPoint] == t[tPoint]:
                sPoint += 1
                tPoint += 1
            else:
                tPoint += 1

        if sPoint == len(s):
            return True
        else: return False
        
        