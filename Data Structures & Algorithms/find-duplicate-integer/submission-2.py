class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                print("num = ", num)
                return num
            seen_nums.add(num)
            