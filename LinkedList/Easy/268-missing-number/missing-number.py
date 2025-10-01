class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        remaining=set()
        for i in range(len(nums)+1):
            remaining.add(i)
        print(remaining)
        for el in nums:
            remaining.discard(el)
        print(remaining)
        for el in remaining:
            return el


        