import random
class RandomizedSet:

    def __init__(self):
        self.randomSet = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.randomSet:
            self.randomSet.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False
        self.randomSet.remove(val)
        return True

    def getRandom(self) -> int:
        index = random.randrange(0, len(self.randomSet))
        
        return list(self.randomSet)[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()