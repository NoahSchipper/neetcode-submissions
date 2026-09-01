class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        x = 0
        while x < len(nums):
            if nums[x] in seen:
                return True
            else: 
                seen.add(nums[x])
            x += 1
        return False