class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token  not in ["*" , "/", "-", "+"]:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                match token:
                    case '*':
                        stack.append(num1 * num2)
                    
                    case '/':
                        stack.append(int(num2 / num1))
        
                    case '-':
                        stack.append(num2 - num1)
            
                    case '+':
                        stack.append(num2 + num1)

        print(stack[-1])            
        return round(stack[-1])

