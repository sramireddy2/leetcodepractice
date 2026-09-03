class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for i, n in enumerate(nums):
            diff = target - n
            if nums[i] in hashtable.keys():
                return [hashtable[nums[i]], i]
            hashtable[diff] = i

        return []




        
        
        
        