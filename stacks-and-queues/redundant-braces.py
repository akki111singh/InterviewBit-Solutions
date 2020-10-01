from collections import deque
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        operators = ["+","-","*","/"]
        stack = deque()
        isred = False
        for ch in A:
            if ch=="(":
                stack.append(0)
            elif ch in operators:
                temp = stack.pop()
                stack.append(temp+1)
            elif ch==")":
                if stack.pop()==0:
                    isred = True
                    break
        return 1 if isred else 0