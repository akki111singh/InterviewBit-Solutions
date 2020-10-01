from collections import deque
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def dfs(root,level,levels,n):
    if root==None:
        return
    if level>n:
        levels.append([])
        n+=1
    levels[-1].append(root.val)
    dfs(root.left,level+1,levels,n)
    

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        levels = []
        dfs(A,1,levels,0)
        return levels
