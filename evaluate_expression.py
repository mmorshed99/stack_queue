#Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
#Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
#Examples:
#
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        total = 0
        for i in A:
            if i == "+" or i == "-" or i == "*" or i == "/":
                a = int(stack[len(stack)-1])
                j = len(stack) - 1
                del stack[j]
                if len(stack) == 0:
                    if i == "-":
                        a = -a
                        stack.append(str(a))
                else:
                    b = int(stack[len(stack)-1])
                    del stack[len(stack)-1]
                    if i == "+":
                        a = b+a
                    if i == "-":
                        a = b-a
                    if i == "*":
                        a = b * a
                    if i == "/":
                        a = b/a
                    stack.append(str(a))
            else:
                stack.append(i)
        return int(stack[0])
