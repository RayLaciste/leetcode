class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first == second:
                continue
            elif -first < -second:
                diff = (-second) - (-first)
                heapq.heappush(stones, -diff)
            
        if stones:
            return -stones[0]
        else:
            return 0
            