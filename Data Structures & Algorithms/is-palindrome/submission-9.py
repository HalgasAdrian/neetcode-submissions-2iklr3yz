class Solution:
    def isPalindrome(self, s: str) -> bool:
        testString = s.lower()
        sList = list(testString)
        front = 0
        back = len(s) -  1

        if len(s) == 0:
            return True

        while front <= back:
            while front < back and not sList[front].isalnum():
                front += 1
            while back > front and not sList[back].isalnum():
                back -= 1
            if sList[front] == sList[back]:
                front += 1
                back -= 1
            else:
                return False 
        
        return True

        