class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        longStr = set()
        for right in range(len(s)):
            while s[right] in longStr:
                longStr.remove(s[left])
                left += 1
            longStr.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
        