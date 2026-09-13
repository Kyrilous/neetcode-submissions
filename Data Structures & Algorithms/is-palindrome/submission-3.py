class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = "".join(s.split())
        cleaned_sentence = re.sub(r'[^a-zA-Z0-9]', '' , sentence).lower()
        left = 0
        right = len(cleaned_sentence) - 1

            ##Debug stuff
        print("Len(cleaned_sentence) = ", len(cleaned_sentence))
        print(cleaned_sentence)
        print(right)

        while(left <= right):
            if(cleaned_sentence[left] != cleaned_sentence[right]):
                return False
            left += 1
            right-= 1
        
        return True
        
    
