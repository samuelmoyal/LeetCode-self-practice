class Solution(object):
    def myAtoi(self, s):
        out=[]
        i=0
        while i<len(s) and s[i]==" ":
            i+=1
        print(out)
        if i<len(s) and (s[i]=="-" or s[i]=="+"):
            start=i
            i+=1
            #while i<len(s) and (s[i]==0 or not s[i].isdigit()):
            #    i+=1
            print(out)
            while i<len(s) and s[i].isdigit():
                out.append(s[i])
                i+=1
            print(out)
            out="".join(out)
            print(out)
            if len(out)>0:
                if int(out)>2**31-1:
                    if s[start]=="+":

                        out=str(2**31-1)
                    else:
                        out=str(2**31)
                
                if s[start]=="+":
                    out=int(out)
                if s[start]=="-":
                    print(out)
                    out=-int(out)
            else:
                return 0

            return out


        elif  i<len(s) and s[i].isdigit():
            print(out)

            while i<len(s) and (s[i]==0 or not s[i].isdigit()):
                i+=1
            while i<len(s) and s[i].isdigit():
                out.append(s[i])
                i+=1
            print(out)
            out="".join(out)
            print(out)
            if len(out)>0:
                if int(out)>=2**31-1:
                    out=2**31-1
                else:
                    out=int(out)
            else:
                return 0
            return out
        else:
            return 0






        
        """
        :type s: str
        :rtype: int
        """
        