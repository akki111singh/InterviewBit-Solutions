class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        result = [[0]*A for i in range(A)]
        
        i,j,di,dj = 0,0,0,1
        
        for k in range(A*A):
            result[i][j] = 1+k
            
            if result[(i+di)%A][(j+dj)%A]:
                di,dj = dj,-di
            
            i += di
            j += dj
        
        return result