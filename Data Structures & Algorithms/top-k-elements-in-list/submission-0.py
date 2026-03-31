from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Count the unique elements within an array, return k most frequent

        Example, 2 then we return the 2 most frequent elements, k = 3
        we return the 3 most frequent elements.

        Required: number of each unique element

        Solution: Use dictionary for quick counts, should be able to use a 
        loop to extract the k most frequent. 
        """
        ans = []
        counts = Counter(nums)
        highCount = counts.most_common() 
        
        for key, value in highCount:
            if len(ans) < k:
                ans.append(key)
            else:
                break 

        return ans
       