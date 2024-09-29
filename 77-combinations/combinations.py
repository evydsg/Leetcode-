class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        value = 1
        self.helper(value, [], combinations, n, k)
        return combinations


    def helper(self, value, currentComb, combinations, n, k):
        if len(currentComb) == k:
            combinations.append(currentComb.copy())
            return
        
        if value > n:
            return 
        
        currentComb.append(value)
        self.helper(value + 1, currentComb, combinations, n, k)
        currentComb.pop()

        self.helper(value + 1, currentComb, combinations, n, k)