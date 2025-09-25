class Solution(object):
    def majorityElement(self, nums):
        freq={}
        M=0
        index=0
        for i, el in enumerate(nums): 
            if el not in freq:
                freq[el]=1
            else: 
                freq[el]+=1
            if freq[el]>M:
                M=freq[el]
                index=i
        return nums[index]
        """
        :type nums: List[int]
        :rtype: int
        """
        