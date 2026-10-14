class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Running a double binary search, first to find the split, second to find our 
        target within the correct split

        [3,4,5,6,1,2]
             ^     ^

        [1,2,3,4,5,6]
             ^     ^
        """
        low, high = 0, len(nums) - 1

        while low < high:
            middle = (low + high) // 2
            if nums[middle] < nums[high]:
                high = middle
            else:
                low = middle + 1
        
        pivot = low

        if target <= nums[-1]:
            low, high = pivot, len(nums) - 1
        else:
            low, high = 0, pivot - 1

        while low <= high:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
        return -1