class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for i, n in enumerate(nums):
            difference = target - n
            if n in hashtable.keys():
                return [hashtable[n], i]
            hashtable[difference] = i
        return []





        
        
        
        