class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A.sort()
        prod1 = A[-1]*A[-2]*A[-3]
        prod2 = A[0]*A[1]*A[2]
        prod3 = A[0]*A[1]*A[-1]
        prod4 = A[0]*A[-2]*A[-1]
        return max(prod1,prod2,prod3,prod4)
