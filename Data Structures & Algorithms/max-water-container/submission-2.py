class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        n = len(heights)
        i=0
        j=n-1

        while i<j:
            area = min(heights[i], heights[j])*(j-i)
            water = area if area > water else water
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return water
            