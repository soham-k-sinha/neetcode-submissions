class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for i in tokens:
            if i in operators:
                num1 = stack.pop()
                num2 = stack.pop()

                if i == '+':
                    result = num2 + num1
                elif i == '-':
                    result = num2 - num1
                elif i == '*':
                    result = num2 * num1
                else:
                    result = int(num2 / num1)
                stack.append(result)
            else:
                stack.append(int(i))
        
        return stack.pop()