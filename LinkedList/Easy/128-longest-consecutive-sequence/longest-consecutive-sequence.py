class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers=set(nums)
        tot=0
        while len(numbers)>0:
            num=numbers.pop()
            count=1
            up=num+1
            down=num-1
            while up in numbers:
                numbers.remove(up)
                up+=1
                count+=1
            while down in numbers:
                numbers.remove(down)
                down+=-1
                count+=1
            tot=max(tot,count)
        return tot