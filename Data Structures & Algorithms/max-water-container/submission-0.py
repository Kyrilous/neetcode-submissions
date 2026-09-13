class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest_volume = 0
        left = 0
        right = len(heights) - 1

        while(left != right):
            container_height = min(heights[left], heights[right])
            current_volume = container_height * (right - left)
            largest_volume = max(largest_volume, current_volume )
            if(heights[left] < heights[right]):
                left += 1
            elif(heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
        return largest_volume
            
        