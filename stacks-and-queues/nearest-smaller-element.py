from collections import deque
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = deque()
        stack.append(-1)
        G = []
        for el in A:
            while stack[-1]>=el:
                stack.pop()
            G.append(stack[-1])
            stack.append(el)
        return G