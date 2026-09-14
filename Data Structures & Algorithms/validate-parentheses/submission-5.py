class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s) <= 1):
            return False

        stack = []
        stack.append(s[0])


        for i in range(1, len(s)):
            if(s[i] == "(" or s[i] == "{" or s[i] == "["):
                stack.append(s[i])
            elif (s[i] == ")" or s[i] == "}" or s[i] == "]"):
                if not stack:
                    return False
                if(s[i] == ")" and stack[-1] != "("):
                    return False
                elif(s[i] == "}" and stack[-1] != "{"):
                    return False
                elif(s[i] == "]" and stack[-1] != "["):
                    return False
                stack.pop()
            print(stack)
        return len(stack) == 0

                

    

