import heapq
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = 0
        heap = []
        heapq.heapify(heap)
        maxx = -1
        A.sort(key=lambda x:x[0])
        for i,el in enumerate(A):
            while n>0 and -1*heap[0]<=el[0]:
                heapq.heappop(heap)
                n-=1
            heapq.heappush(heap,-1*el[1])
            n+=1
            if n>maxx:
                maxx=n
        return maxx