class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=nums[0]
        prefix=[1]
        for i in range(1,len(nums)):
            prefix.append(p)
            p=p*nums[i]
        suffix=[1]
        s=nums[-1]
        for i in range(1,len(nums)):
            suffix.append(s)
            s=s*nums[len(nums)-1-i]
        answer=[]
        for i in range(len(nums)):
            answer.append(prefix[i]*suffix[len(nums)-1-i])
        return answer



            

        