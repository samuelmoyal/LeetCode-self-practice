class Solution(object):
    def removeElement(self, nums, val):
        out=0
        for el in nums:
            if el !=val:
                nums[out]=el
                out+=1
        return out 
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        