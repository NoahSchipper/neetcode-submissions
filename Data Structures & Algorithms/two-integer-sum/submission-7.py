class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            difference = target - nums[i]
            if difference in nums and nums.index(difference) != i:
                return sorted([i, nums.index(difference)])
            i += 1
