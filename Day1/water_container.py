from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        largest = 0
        while i < j:
            largest = max(largest, ((j-i) * min (heights[i], heights[j])))
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return largest
