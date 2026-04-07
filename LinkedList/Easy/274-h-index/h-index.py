class Solution(object):
    def hIndex(self, citations):
        out=[0]*1001
        for i in range(len(citations)):
            for j in range((citations[i]+1)):
                out[j]+=1
        i=0
        print(out[:10])
        while out[i]>=i:
            i+=1
        return i-1

        


        """
        :type citations: List[int]
        :rtype: int
        """
        