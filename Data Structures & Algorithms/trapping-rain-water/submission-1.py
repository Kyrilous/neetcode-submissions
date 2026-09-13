class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        # Arrays to track the largest wall to the 
        # left and right of any given index
        leftMax = [0] * n
        rightMax = [0] * n

        # Index 0 has nothing before it, 
        # set its leftMax to it's own height
        leftMax[0] = height[0]
        
        # For each index, store the tallest height seen 
        # so far from the left.
        # If the current height is taller than the previous maximum,
        # update the maximum to the current height.
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]

        # Do the same thing except now we check tallest height 
        # seen from the right. Once we have both of these values, we can
        # calculate volume at each index and sum them.
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        water = 0
        # At every index, the smaller wall to the left and 
        # right creates an upper bound how much water this space can hold.
        # The ammount of water that can be stored simple becomes: 
        # (Height of smaller wall) - (Mass taking up space at this index)
        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]
        return water