class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        for key in seen:
            if seen[key] > len(nums) // 2:
                return key
        