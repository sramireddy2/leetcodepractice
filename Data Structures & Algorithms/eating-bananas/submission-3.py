class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2

            ttime = 0
            for p in piles:
                ttime += math.ceil(float(p) / mid)

            if ttime <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res