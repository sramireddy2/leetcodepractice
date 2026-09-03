class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        countk = nums.count(k)
        res = 0

        for i in range(1, 51):
            count = 0
            if i == k:
                continue
            for num in nums:
                if num == i:
                    count += 1
                if num == k:
                    count -= 1
                count = max(count, 0)
                res = max(res, countk + count)

        return res

            