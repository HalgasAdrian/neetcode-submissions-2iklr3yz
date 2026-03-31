class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        counts = []
        current_len = 1  # length of current consecutive run

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                # duplicate: skip it, do not break the current run nor extend it
                continue
            elif nums[i + 1] == nums[i] + 1:
                # consecutive: extend current run
                current_len += 1
            else:
                # gap: store current run and reset
                counts.append(current_len)
                current_len = 1

        # append the last run
        counts.append(current_len)

        return max(counts)