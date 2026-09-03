class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        num = x
        
        while num:
            reverse = reverse * 10 + num % 10
            num //= 10

        return reverse == x
        