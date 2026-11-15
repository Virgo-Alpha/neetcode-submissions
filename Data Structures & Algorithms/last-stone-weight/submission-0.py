class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        We always need to repeatedly remove the two heaviest stones.
        A max-heap is perfect for this because it lets us efficiently
            extract the largest values.

        Most languages provide min-heaps, so a common trick is to store negative values.
        This makes the smallest (most negative) value represent the largest stone.
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])