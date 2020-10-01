class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    
    def diagonal(self, A):
        res = []
        temp = []
        for s in range(2*(len(A)-1)+1):
            temp = []
            for i in range(0,s+1):
                j = s-i
                if i>=len(A) or s-i >=len(A) :
                    continue
                temp.append(A[i][j])
            res.append(temp)
        return res
            