class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashtable:
                return [hashtable[difference], i]
            hashtable[n] = i




        
        
        
        