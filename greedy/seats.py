class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        pos = []
        MOD = 10000003
        for i,ch in enumerate(A):
            if ch=='x':
                pos.append(i)
        n = len(pos)
        middle = (n-1)//2
        moves = 0
        for i in range(n):
            if i<middle:
                moves += abs( (pos[middle] - (middle-i) ) - pos[i])%MOD
            elif i>middle:
                moves += abs( pos[i] - (pos[middle]+(i-middle)) )%MOD
        return moves%MOD