class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        return map(list,zip(*A[::-1]))
 
