class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        f
        """
        seen = []
        maxLength = 1
        left = 0
        right = 1

        if len(s) == 0:
            return 0

        while right < len(s):
            seen.append(s[left])
            if s[right] not in seen:
                seen.append(s[right])
                currentMax = right - left + 1
                if currentMax > maxLength:
                    maxLength = currentMax
                right += 1
            elif s[right] in seen:
                seen = []
                left += 1
                right = left + 1

        return maxLength
