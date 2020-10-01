class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        moves = 0
        for i,el in enumerate(A):
            if (moves%2==0 and el==0) or (moves%2==1 and el==1):
                moves+=1
        return moves
