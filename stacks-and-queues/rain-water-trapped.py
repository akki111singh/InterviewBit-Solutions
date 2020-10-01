class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        maxleft = []
        maxright = []
        maxi = 0
        for el in A:
            maxleft.append(maxi)
            maxi = max(maxi,el)
        maxi = 0
        for el in A[::-1]:
            maxright.append(maxi)
            maxi = max(maxi,el)
        maxright = maxright
                