from collections import deque
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        
        i,j=C-1,D-1
        queue=deque([((i,j),0)])
        
        final=set()
        final.add((i,j))
        while(bool(queue)):
            pre=queue.pop()
            i,j=pre[0][0],pre[0][1]
            dist=pre[1]
            
            if (i,j)==(E-1,F-1):
                return dist
            
            xarr=[-1,-2,-2,-1,1,2,2,1]
            yarr=[-2,-1,1,2,2,1,-1,-2]
            
            for k in range(8):
                x,y=i+xarr[k],j+yarr[k]
                if(x>=0 and x<A and y>=0 and y<B):
                    if((x,y) not in final):
                        final.add((x,y))
                        queue.appendleft(((x,y),dist+1))
            
        
        return -1
