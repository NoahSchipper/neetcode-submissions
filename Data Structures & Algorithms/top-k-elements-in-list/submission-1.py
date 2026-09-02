class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        x = 0
        while x < len(nums):
            if nums[x] not in counts:
                counts[nums[x]] = 1
            else:
                counts[nums[x]] += 1
            x += 1
        top = sorted(counts.items(), key=lambda item: item[1], reverse=True)[:k]
        top_numbers = [item[0] for item in top]        
        return top_numbers