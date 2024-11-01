import random
class RandomizedSet:

    def __init__(self):
        self.randomSet = set()
        
    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        else:
            self.randomSet.add(val)
        
    def remove(self, val: int) -> bool:
        try:
            self.randomSet.remove(val)
            return True
        except KeyError:
            return False
        
    def getRandom(self) -> int:
        randomElement = random.sample(list(self.randomSet), 1)[0]
        return randomElement

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()