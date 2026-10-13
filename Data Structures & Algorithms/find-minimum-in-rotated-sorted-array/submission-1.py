class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        target = nums[0]

        while low <= high:
            if nums[low] < nums[high]:
                target = min(target, nums[low])
                break

            middle = (low + high) // 2
            target = min(target, nums[middle])
        
            if nums[middle] >= nums[low]:
                low = middle + 1
            else:
                high = middle - 1
        return target
