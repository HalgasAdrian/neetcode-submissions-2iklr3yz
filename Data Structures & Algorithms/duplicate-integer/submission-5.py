class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Sort the array, run a pointer through it, if pointer == pointer + 1:
        return True

        if we make it through the list and see nothing we can return False
        """
        pointer = 0
        nums.sort()
        
        while pointer < len(nums) - 1:
            if nums[pointer] == nums[pointer + 1]:
                return True
            else:
                pointer += 1

        return False 
        