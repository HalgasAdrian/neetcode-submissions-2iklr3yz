class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        end = len(arr) - 1
        slow = 0
        fast = 1
        maxVal = 0

        while slow < end:
            if fast < len(arr):
                if arr[fast] > maxVal:
                    maxVal = arr[fast]
                fast += 1
            else:
                arr[slow] = maxVal
                slow += 1
                fast = slow + 1
                maxVal = 0

        arr[end] = -1
        return arr