class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffmap = {}

        for i in range(len(nums)):
            if nums[i] in diffmap:
                return [diffmap[nums[i]], i]

            diffmap[target - nums[i]] = i
        





        
        
        
        