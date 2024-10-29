class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyStore:
            self.keyStore[key].append([value, timestamp])
        else:
            self.keyStore[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.keyStore.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            middle = (left + right) // 2

            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        
        return result
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)