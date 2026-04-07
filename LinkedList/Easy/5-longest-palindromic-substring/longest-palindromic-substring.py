class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==0:return ""
        if len(s)==1:return s
        out=s[0]
        M=1
        for idx in range(len(s)):
            if idx==0:
                if s[idx+1]==s[idx] and M<2:
                    out=s[0:2]
                    M=2
            if 1<=idx and idx<len(s)-1:
                m=1
                i=idx-1
                j=idx+1
                while j<len(s) and i>=0 and s[i]==s[j]:
                    m+=2
                    i=i-1
                    j=j+1
                if m>M:
                    out=s[i+1:j]
                    M=m
                i=idx
                j=idx+1
                m=0
                while j<len(s) and i>=0 and s[i]==s[j]:
                    m+=2
                    i=i-1
                    j=j+1
                if m>M:
                    out=s[i+1:j]
                    M=m
            if idx==len(s)-1:
                if s[idx-1]==s[idx] and M<2:
                    out=s[idx-1:idx+1]
                    M=2
        return out
            
            
                







            


        """
        :type s: str
        :rtype: str
        """
        