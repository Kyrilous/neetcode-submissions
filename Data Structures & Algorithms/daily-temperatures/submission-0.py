class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = 0
        weather_stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while weather_stack and temperatures[weather_stack[-1]] < temperatures[i]:
                old_index = weather_stack.pop()
                res[old_index] = i - old_index
            weather_stack.append(i)
        return res

