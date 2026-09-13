class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        encounter_tracker = {}

        for num in nums:
            if num not in encounter_tracker:
                encounter_tracker[num] = 1
            else:
                encounter_tracker[num] += 1

        res = []

        for _ in range(k):
            max_num = max(encounter_tracker, key=encounter_tracker.get)

            res.append(max_num)

            del encounter_tracker[max_num]

        return res