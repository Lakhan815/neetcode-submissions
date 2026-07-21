class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        cur = 0
        for i in range(len(heights)):
            for j in range(len(heights)-1,i,-1):
                cur = min(heights[i],heights[j])*(j-i)
                if(cur>res):
                    res=cur
        return res