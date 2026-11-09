class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

       if len(s1) > len(s2):
        return False

       window_count = [0] * 26
       s1_count = [0] * 26
       
       for letter in s1:
        s1_count[ord(letter) - ord('a')] += 1

    
       l = 0
       r = len(s1)
        
       while r <= len(s2):
            for letter in s2[l:r]:
                window_count[ord(letter) - ord('a')] += 1
            if window_count == s1_count:
                return True
            window_count = [0] * 26
            l = l + 1
            r = r + 1
       return False
            








         



        