from collections import deque

class TreeNode:
    def __init__(self):
        self.adj = []
        self.visited = False

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        nodes = []
        for i in range(n):
            nodes.append(TreeNode())
        for i,el in enumerate(A):
            if el!=-1:
                nodes[i].adj.append(A[i])
                nodes[el].adj.append(i)
        maxfirst = -1
        dist = -1
        stack = deque()
        nodes[0].visited = True
        stack.append((0,0))
        while stack:
            el = stack.pop()
            if el[1]>dist:
                maxfirst = el[1]
                dist = el[1]
            for i in nodes[el[0]].adj:
                if nodes[i].visited==False:
                    nodes[i].visited = True
                    stack.append((i,el[1]+1))
        
        for i in range(n):
            nodes[i].visited = False
        
        maxsecond = -1
        dist = -1
        stack.clear()
        nodes[maxfirst].visited = True
        stack.append((maxfirst,0))
        while stack:
            el = stack.pop()
            if el[1]>dist:
                dist = el[1]
            for i in nodes[el[0]].adj:
                if nodes[i].visited==False:
                    nodes[i].visited = True
                    stack.append((i,el[1]+1))
                    
        return dist
        