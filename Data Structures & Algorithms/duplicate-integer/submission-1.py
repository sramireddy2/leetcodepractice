class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set(nums)
        if len(new_nums) != len(nums):
            return True
        return False

         
        