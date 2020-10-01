class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
      dp = []
      dp.append(A[0])
      
      for i in range(1,len(A)):
         dp.append(max(A[i]+dp[i-1],A[i]))
      
      return max(dp)