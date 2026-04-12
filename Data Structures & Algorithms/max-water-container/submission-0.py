class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        maximum = 0

        while l < r:
            total = min(heights[l],heights[r]) *(r-l)
            maximum = max(maximum,total)
            
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1



        return maximum         