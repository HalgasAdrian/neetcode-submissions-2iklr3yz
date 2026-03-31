class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Easiest way to solve this is using two pointers
        which are moving in same direction,

        if pointers are the same, advance them
        """

        left = 0
        right = 0

        word1 = list(s)
        word2 = list(t)

        word1.sort()
        word2.sort()   

        if len(word1) != len(word2):
            return False

        while left < len(word1):
            if word1[left] != word2[right]:
                return False
            else:
                left += 1
                right += 1
        return True
        



        