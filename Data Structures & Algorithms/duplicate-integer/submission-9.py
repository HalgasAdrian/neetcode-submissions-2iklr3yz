class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        nput: nums = [1, 2, 3, 3]
                            ^ 
                               ^
        """
        nums.sort()
        pointer1 = 0
        pointer2 = 1

        while pointer2 <= len(nums) - 1:
            if nums[pointer1] == nums[pointer2]:
                return True
            else:
                pointer1 += 1
                pointer2 += 1
        
        return False 
        