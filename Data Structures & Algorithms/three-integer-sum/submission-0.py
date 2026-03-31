from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            # skip duplicate anchors
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            middle = i + 1
            right = len(nums) - 1

            while right > middle:
                s = nums[i] + nums[middle] + nums[right]

                if s == 0:
                    # append VALUES (your version was appending the index i)
                    ans.append([nums[i], nums[middle], nums[right]])

                    right -= 1
                    middle += 1

                    # skip duplicates for middle/right after a match
                    while right > middle and nums[middle] == nums[middle - 1]:
                        middle += 1
                    while right > middle and nums[right] == nums[right + 1]:
                        right -= 1

                elif s > 0:
                    right -= 1
                elif s < 0:
                    middle += 1
                else:
                    break

        return ans
