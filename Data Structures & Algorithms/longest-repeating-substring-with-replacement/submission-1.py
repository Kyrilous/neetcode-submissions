class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        
        longest = 1
        char_count = [0] * 26
       
        # window = []
        # window.append(s[0])
        
        char_count[ord(s[0]) - ord('A')] += 1

        while r < len(s):
            letter = s[r]
            # window.append(letter)
            window_size = r - l + 1
            
            char_count[ord(letter) - ord('A')] += 1
            most_frequent = max(char_count)
            replacments = window_size - most_frequent
            
            if replacments <= k and longest < window_size:
                longest = window_size
                
            
            elif replacments > k:
                char_count[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1

        return longest

                       