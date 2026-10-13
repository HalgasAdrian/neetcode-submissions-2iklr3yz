class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        nums = [3,4,5,6,1,2], target = 1
                ^   ^     ^
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            middle = (low + high) // 2
            
            if nums[middle] == target:
                return middle
            
            # Check if the left half is sorted
            if nums[low] <= nums[middle]:
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            # Otherwise, the right half must be sorted
            else:
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
        
        return -1
