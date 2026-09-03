class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        streak = 0

        for num in numSet:
            if len(numSet) == 1:
                streak = 1
                return streak

            elif num -1 not in numSet:
                currentNum = num
                currentStreak = 1

                while currentNum + 1 in numSet:
                    currentNum += 1
                    currentStreak += 1

                streak = max(streak, currentStreak)
        return streak



        
        
            
        