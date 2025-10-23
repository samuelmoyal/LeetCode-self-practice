class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen=[0]*(len(nums))
        for num in nums:
            if num>0 and num<len(nums)+1:
                if seen[num-1]==0:
                    seen[num-1]+=1
        for i in range(len(seen)):
            if seen[i]==0:
                return i+1
        return len(nums)+1
            

        