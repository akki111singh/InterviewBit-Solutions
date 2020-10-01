import heapq
class Node:
    def __init__(self):
        self.key = float('inf')
        self.adj = []
        self.visited = False
    def __lt__(self,other):
        return self.key<other.key

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        nodes = []
        for i in range(A):
            nodes.append(Node())
        for row in B:
            nodes[row[0]-1].adj.append([row[1]-1,row[2]])
            nodes[row[1]-1].adj.append([row[0]-1,row[2]])
        
        nodes[0].key = 0
        weight = 0
        heap = [(0,0)]
        heapq.heapify(heap)
        n = 0
        while n<A:
            cost,prevnode = heapq.heappop(heap)
            if nodes[prevnode].visited:
                continue
            nodes[prevnode].visited = True
            n+=1
            weight += cost
            for edge in nodes[prevnode].adj:
                if nodes[edge[0]].visited == False:
                    nodes[edge[0]].key = min(nodes[edge[0]].key,edge[1])
                    heapq.heappush(heap,(nodes[edge[0]].key,edge[0]))
        
        return weight
