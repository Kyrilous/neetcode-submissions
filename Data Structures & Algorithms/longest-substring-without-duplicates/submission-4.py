class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        longest = 0
        seen_chars = set()

        for right in range(len(s)):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            seen_chars.add(s[right])
            longest = max(longest, right - left + 1)

        return longest