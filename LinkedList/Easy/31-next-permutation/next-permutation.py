class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums)>1:

            i=len(nums)-1
            last_digit=[nums[i]]
            while i>0 and nums[i-1]>=nums[i]:
                last_digit.append(nums[i-1])
                i=i-1
            if i==0:
                nums.reverse()
            else:
                j=0
                while last_digit[j]<=nums[i-1]:
                    j+=1
                new=last_digit[j]
                last_digit[j]=nums[i-1]
                nums[i-1]=new
                nums[i:]=last_digit
        """
        Do not return anything, modify nums in-place instead.
        """
        