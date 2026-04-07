class Solution(object):
    def convert(self, s, numRows):
        if numRows==0:
            return ""
        if numRows==1:
            return s

        grid=[[0]*int(len(s)) for i in range(numRows)]
        i=0
        j=0
        for l in s:
            grid[i][j]=l
            if j%(numRows-1)==0 and i<numRows-1:
                i+=1
            else:
                i-=1
                j+=1
        out=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    out.append(grid[i][j])
        return "".join(out)
                    
                
            

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        