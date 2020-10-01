class Solution:
    # @param A : integer
    # @return a list of integers
   
    def getRow(self, A):
        row = [1]
        
        for i in range(A):
            row = [x+y for x,y in zip([0]+row,row+[0])]
        return row
