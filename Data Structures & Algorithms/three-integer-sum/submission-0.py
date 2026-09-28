class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = []
        for x in range(0, len(nums) - 2):
            left = x + 1
            right = len(nums) - 1
            while left < right:
                currSum = nums[left] + nums[right]
                if currSum == nums[x] * -1:
                    currTrip = [nums[x], nums[left], nums[right]]
                    if currTrip not in trips:
                        trips.append(currTrip)
                    left += 1
                    right -= 1
                elif currSum > nums[x] * -1:
                    right -= 1
                else:
                    left += 1
        return trips
                
