class Solution:
    def trap(self, height: List[int]) -> int:
        start = -1
        water = 0

        for i in range(len(height)):
            if height[i] > 0:
                start = i
                break

        if start == -1:
            return 0

        left = start

        while left < len(height) - 1:

            right = left + 1
            best_right = right

            # Look for a wall as tall as left
            while right < len(height):
                if height[right] >= height[left]:
                    best_right = right
                    break

                # Otherwise remember the tallest wall we've seen
                if height[right] > height[best_right]:
                    best_right = right

                right += 1

            # Calculate water between left and best_right
            water_level = min(height[left], height[best_right])

            for i in range(left + 1, best_right):
                water += water_level - height[i]

            left = best_right

        return water