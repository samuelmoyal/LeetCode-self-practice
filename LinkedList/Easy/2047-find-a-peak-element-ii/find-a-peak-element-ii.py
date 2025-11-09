class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        if len(mat)>0:
            seen=set()
            cands=[(0,0)]
            while len(cands)>0:
                print(cands)
                test=cands.pop()
                i,j=test
                if i+1<len(mat) and (i+1,j) not in seen:
                    if mat[i+1][j]>mat[i][j]:
                        cands.append((i+1,j))
                        seen.add((i,j))
                    else:
                        seen.add((i+1,j))
                if i-1>=0 and (i-1,j) not in seen:
                    if mat[i-1][j]>mat[i][j]:
                        cands.append((i-1,j))
                        seen.add((i,j))
                    else:
                        seen.add((i-1,j))
                if j+1<len(mat[0]) and (i,j+1) not in seen:
                    if mat[i][j+1]>mat[i][j]:
                        cands.append((i,j+1))
                        seen.add((i,j))
                    else:
                        seen.add((i,j+1))
                if j-1>=0 and (i,j-1) not in seen:
                    if mat[i][j-1]>mat[i][j]:
                        cands.append((i,j-1))
                        seen.add((i,j))
                    else:
                        seen.add((i,j-1))
                if (i,j) not in seen:
                    return [i,j]
        else:
            return O 
        
        