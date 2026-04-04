class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        keep track of a count, use a nested loop to see if we have a +1 
        """
        count = 0

        for i in arr:
            if (i + 1) in arr:
                count +=1 

        return count