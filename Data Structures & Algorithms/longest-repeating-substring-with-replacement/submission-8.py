class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return 1

        l = 0
        r = 1
        char_count = [0] * 26
        char_count[ord(s[0]) - ord('A')] += 1
        longest = 1

        while r < len(s):
            letter = s[r]
            char_count[ord(letter) - ord('A')] += 1
            window_size = r - l + 1
            replacments = window_size - max(char_count)
            if replacments > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1

            elif replacments <= k:
                longest = max(longest, window_size)
            r += 1

        return longest


 

                       