from collections import deque
class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        maxarea = 0
        stack = deque()
        stack.append(-1)
        left = []
        for ind,el in enumerate(A):
            if stack[-1]==-1:
                left.append(-1)
                stack.append(ind)
            else:
                while A[stack[-1]]>=el and stack[-1]!=-1:
                    stack.pop()
                left.append(stack[-1])
                stack.append(ind)
        
        stack.clear()
        stack.append(-1)
        right = []
        n = len(A)
        
        for ind,el in enumerate(A[::-1]):
            if stack[-1]==-1:
                right.append(-1)
                stack.append(n-1-ind)
            else:
                while A[stack[-1]]>=el and stack[-1]!=-1:
                    stack.pop()
                right.append(stack[-1])
                stack.append(n-1-ind)
        right = right[::-1]
        for i in range(n):
            templ = left[i]
            tempr = right[i] if right[i]!=-1 else n
            area = A[i] * (tempr-templ-1)
            if area>maxarea:
                area = maxarea
        return maxarea
