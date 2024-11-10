class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differences = []
        cost = 0

        for cA, cB in costs:
            differences.append([cB - cA, cA, cB])

        differences.sort()

        for index in range(len(differences)):
            if index < len(differences) / 2:
                cost += differences[index][2]
            else:
                cost += differences[index][1]

        return cost