class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Trick here is to use a set to track unique characters
        """
        longestSubstring = 0
        unique = set()
        left = 0

        for right in range(len(s)):
            # Duplicate remove and shrink
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            # Expand window
            unique.add(s[right])
            longestSubstring = max(longestSubstring, right - left + 1)

        return longestSubstring
