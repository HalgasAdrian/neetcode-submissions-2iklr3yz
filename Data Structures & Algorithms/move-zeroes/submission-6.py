class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        nums = [0,0,1,2,0,5]
                ^
                    ^
        """
        l = 0
        r = 1

        for r in range(len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            elif nums[l] != 0 and nums[r] == 0:
                l += 1
                r += 1
            else:
                l += 1

        