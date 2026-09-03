class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currentsum = 0
        prefixsum = {0:1}

        for num in nums:
            currentsum += num
            diff = currentsum - k

            res += prefixsum.get(diff, 0)
            prefixsum[currentsum] = 1 + prefixsum.get(currentsum, 0)

        return res