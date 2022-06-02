class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R,  0, None) for _, R, _ in buildings}))
        result, hp = [[0, 0]], [(0, float("inf"))]
        
        for x, negH, R in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if result[-1][1] + hp[0][0]:
                result += [x, -hp[0][0]],
        return result[1:]
                