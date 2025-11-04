class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        tot=(j-i)*min(height[i],height[j])
        while i<j:
            while i<j and height[i]<=height[j]:
                tot=max((j-i)*min(height[i],height[j]),tot)
                i+=1
            while i<j and height[i]>height[j]:
                tot=max((j-i)*min(height[i],height[j]),tot)
                j+=-1
        return tot
            


        