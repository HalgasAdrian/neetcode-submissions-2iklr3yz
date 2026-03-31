class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Use a pointer and a loop

        the pointer will keep track of nums1

        then use the loop to find nums1 in nums2 

        append to ans 
        """
        pointer = 0
        ans = []

        while pointer < len(nums1):
            for i in range(len(nums2)):
                if nums1[pointer] == nums2[i]:
                    ans.append(i)
                    break
            pointer += 1
                
        return ans
        