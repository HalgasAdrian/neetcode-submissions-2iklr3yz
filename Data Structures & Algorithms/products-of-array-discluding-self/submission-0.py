import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Division solution: multiply everything together,
        then using divide by each index and append result
        """
        total = math.prod(nums)
        ans = []

        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(int(total/nums[i]))
            else:
                temp = nums.copy()
                temp.pop(i)
                ans.append(math.prod(temp))
            

        return ans

