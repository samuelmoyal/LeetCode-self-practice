class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        # skip spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # sign
        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1
        
        res = 0
        
        # parse digits
        while i < n and s[i].isdigit():
            d = int(s[i])
            
            # overflow check
            if res > (2**31 - 1 - d) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            res = res * 10 + d
            i += 1
        
        return sign * res





        
        """
        :type s: str
        :rtype: int
        """
        