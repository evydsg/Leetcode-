class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0:
            return 0
        
        frequency = Counter(tasks)
        maxHeap = [-count for count in frequency.values()]
        heapq.heapify(maxHeap)
        time = 0
        queue = []

        while maxHeap or queue:
            time += 1

            if maxHeap:
    
                count = 1 + heapq.heappop(maxHeap)

                if count != 0:
                    queue.append([count, time + n])
            
            if queue and queue[0][1] == time:
                count, time = queue.pop(0)
                heapq.heappush(maxHeap, count)
            
        return time