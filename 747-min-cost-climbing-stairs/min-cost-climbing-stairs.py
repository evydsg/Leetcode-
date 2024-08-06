class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        end = len(cost)
        cost.append(0)
        cost.append(0)
        for i in range(end):
            end -= 1
            cost[end] = min(cost[end + 1],cost[end + 2]) + cost[end]
        return min(cost[0],cost[1])
        