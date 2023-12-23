# leetcode 150) Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens):
        # tokens = ["2", "1", "+", "3", "*"]
        # 2 1 +  (2 + 1)  push [3] 
        # [3, 3] * (3 * 3) = 9 <- res 

        ops = ["+", "-", "*", "/"]
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ops:
                num = int(tokens[i])
                stack.append(num)
                # print(stack)

            else:
                # if is "+" or "-" or "*" or "/"
                if tokens[i] == "+":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = num1 + num2
                    stack.append(res)
                    # print(stack)
                elif tokens[i] == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = num1 - num2
                    stack.append(res)
                    # print(stack)
                elif tokens[i] == "*":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    res = num1 * num2
                    stack.append(res)
                    # print(stack)
                elif tokens[i] == "/":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    if num2 != 0:
                        res = int(num1 / num2)

                    stack.append(res)

        return stack.pop()

        # stack = [22]
            # + (pop x2) 9 and 3 = 12  [10, 6, 12]
            # * (pop x2) 12 and -11 = -132  [10, 6, -132] 
            # / (pop x2) 6 and -132 = 0 [10, 0] 6 // -132 
            # * (pop x2) 10 and 0 = 0
            # + (pop x2) 0 and 17 = 17
            # + (pop x2) 17 and 5 = 22


tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(Solution().evalRPN(tokens))

tokens = ["4","-2","/","2","-3","-","-"]
print(Solution().evalRPN(tokens))
# stack = [4, -2]
#     / : pop x2: 4 / -2 = -2
#     stack = [-2, 2, -3]
#     - : pop x2: 2 - (-3) = 5
#     stack = [-2, 5]
#     - : pop x2: -2 - 5 = -7
    
