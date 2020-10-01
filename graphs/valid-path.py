def dist(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def outofbounds(x1,y1,x,y):
    if x1>x or x1<0 or y1>y or y1<0:
        return True
    else:
        return False
    
    
def dfs(x1,y1,mat,x,y):
    mat[x1][y1] = 1
    if outofbounds(x1,y1,x,y):
        return False
    if x1==x and y1==y:
        return True
    neighbours = [(x1-1,y1),(x1+1,y1),(x1,y1+1),(x1,y1-1),(x1-1,y1-1),(x1+1,y1+1),(x1-1,y1+1),(x1+1,y1-1)]
    res = False
    for n in neighbours:
        if outofbounds(n[0],n[1],x,y)==False and mat[n[0]][n[1]]==0:
            res = res or dfs(n[0],n[1],mat,x,y)
    return res

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        mat = []
        x = A
        y = B
        N = C
        R = D
        cx = E
        cy = F
        for i in range(A+1):
            mat.append([])
            for j in range(B+1):
                mat[-1].append(0)
        for c in range(N):
            for i in range(x+1):
                for j in range(y+1):
                    if dist([i,j],[cx[c],cy[c]])<=R**2:
                        mat[i][j] = -1
        if mat[x][y]==-1:
            return "NO"
        else:
            return "YES" if dfs(0,0,mat,x,y) else "NO"
                    
