from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        A = A.split("/")
        stack = deque()
        for ch in A:
            if ch=='.':
                continue
            else:
                if ch=="..":
                    stack.pop()
                else:
                    stack.append(ch)
        return "/".join(list(stack))