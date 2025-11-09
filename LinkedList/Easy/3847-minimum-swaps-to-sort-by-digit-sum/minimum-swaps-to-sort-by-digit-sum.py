class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        digits=[]
        for i in range(len(nums)):
            count=0
            char=str(nums[i])
            for digit in char:
                count+=int(digit)
            digits.append((count,nums[i]))
        digits_sorted=sorted(digits)
        dico={}
        for i in range(len(digits_sorted)):
            digit=digits_sorted[i]
            dico[digit]=i
        i=0
        count=0
        while i<len(nums)-1:
            digit=digits[i]
            rank=dico[digit]
            if rank !=i:
                trans=digit
                digits[i]=digits[rank]
                digits[rank]=digit
                count+=1
            else:
                i+=1
        return count

                
        



        
        