class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = 0

        while left <= right:
            mid = (left + right) // 2

            totaltime = 0

            for p in piles:
                totaltime += math.ceil(float(p)/mid)

            if totaltime <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result





        