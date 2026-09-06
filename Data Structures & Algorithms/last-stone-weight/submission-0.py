class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            firststone = heapq.heappop(stones)
            secondstone = heapq.heappop(stones)
            if secondstone != firststone:
                heapq.heappush(stones, firststone - secondstone)

        stones.append(0)
        return abs(stones[0])



        