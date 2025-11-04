class Solution:
    def countBits(self, n: int) -> List[int]:
        out=[0]*(n+1)
        m=0
        while 2**(m+1)<=n:
            out[int(2**m):int(2**(m+1))]=[1+x for x in out[0:2**m]]
            m+=1
        out[int(2**m):n+1]=[1+x for x in out[0:n+1-int(2**m)]]
        return out
        