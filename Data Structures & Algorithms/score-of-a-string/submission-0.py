class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Initialize an output we will return

        Loop through the array, get the abs(val - nextVal)

        Add the result to our output and return it at the end
        """
        result = 0
        myList = list(s)

        if len(s) == 0:
            return 0
        
        for i in range(len(myList) - 1):
            total = abs(ord(myList[i]) - ord(myList[i + 1]))
            result = result + total

        return result
        