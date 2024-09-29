class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        differences = []
        result = 0

        for cA, cB in costs:
            differences.append([cB - cA, cA, cB])
        
        differences.sort()
        
        for index in range(len(costs)):
            if index < len(differences)//2:
                result += differences[index][2]
            else:
                result += differences[index][1]
        
        return result