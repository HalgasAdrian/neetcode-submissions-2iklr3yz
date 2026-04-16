class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Practice a brute force solution

        Will involve a nested for loop
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
      
        