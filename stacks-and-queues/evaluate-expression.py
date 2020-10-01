from collections import deque
class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = deque()
        operators = ["+","*","/","-"]
        for ch in A:
            if ch not in operators:
                stack.append(int(ch))
            else:
                o1 = stack.pop()
                o2 = stack.pop()
                if ch=="*":
                    stack.append(o1*o2)
                elif ch=="+":
                    stack.append(o1+o2)
                elif ch=="-":
                    stack.append(o1-o2)
                elif ch=="/":
                    stack.append(o1//o2)
        return stack.pop()
            