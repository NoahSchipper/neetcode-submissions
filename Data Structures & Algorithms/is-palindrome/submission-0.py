class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = "".join(char for char in s if char.isalnum()).lower()
        left = 0
        right = len(cleanStr) - 1
        while left < right:
            if cleanStr[left] == cleanStr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
