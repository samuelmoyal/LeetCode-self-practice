class Solution(object):
    def generateParenthesis(self, n):
        if n==1:
            return ["()"]
        if n==0:
            return [""]
        if n>1:
            out=set()
            for el in self.generateParenthesis(n-1):
                out.add("()"+el)
                out.add("("+el+")")
                out.add(el+"()")
                right=0
                left=0
                idx=[]
                for i in range(len(el)):
                    if left==right:
                        idx.append(i)
                    if el[i]=="(":
                        right+=1
                    if el[i]==")":
                        left+=1
                for i in range(len(idx)):
                    for j in range(i,len(idx)):
                        out.add(el[:idx[i]]+"("+el[idx[i]:idx[j]]+")"+el[idx[j]:])
                
                to_del=set()
                
                for el in out:
                    if len(el)!=2*n:
                        to_del.add(el)
                for el in to_del:
                    out.discard(el)



            out=list(out)
            
            
            return out

            
        """
        :type n: int
        :rtype: List[str]
        """
        