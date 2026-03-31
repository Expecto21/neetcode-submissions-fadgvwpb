class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxWater=0

        while l<r:
            water=min(heights[l],heights[r])*(r-l)

            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
            
            maxWater=max(water,maxWater)
        
        return maxWater
