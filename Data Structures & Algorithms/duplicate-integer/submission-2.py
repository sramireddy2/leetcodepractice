class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newnums = set(nums)
        return len(newnums) < len(nums)

        
    
        