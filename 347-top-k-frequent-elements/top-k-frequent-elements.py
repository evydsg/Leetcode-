import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
            Understand
                - The idea is to return the k most frequent elements
                
                Questions
                    - Can we have an empty array?
                    - Can k be a negative number?
                    - Can k be greater than the length of the list?

            Match
                - Use dictionary to keep track of how many times it shows up
            
            Plan
                Count the Frequency of Each Element:    
                    - Use a hash map (or dictionary) to count how many times each element appears in the array.
                    - Iterate through the array and update the frequency count for each element.
                Initialize a Min-Heap:
                    - Use a min-heap to keep track of the top k most frequent elements.
                    - The heap will store tuples of the form (frequency, element).
                Build the Heap:
                    - Iterate through the frequency map.
                    - For each element and its frequency, push a tuple (frequency, element) into the heap.
                    - If the size of the heap exceeds k, remove the smallest element (the root of the heap).
                    - This ensures that the heap only contains the k most frequent elements at any given time.
                Extract the Top k Elements:
                    - Once all elements have been processed, the heap will contain the k most frequent elements.
                    - Extract these elements from the heap.
                Return the Result:
                    - Collect the elements from the heap into a list and return this list as the result.
        """

        frequency = Counter(nums) #Count how many times each element appears

        heap = [] #Initialize a heap to keep track of the top k elements

        for num, freq in frequency.items(): #Using both key and value
            heapq.heappush(heap, (freq, num))#Push to the heap the number and its frequency

            if len(heap) > k: #Eliminate the smallest element
                heapq.heappop(heap)

        top_k_elements = [num for frequency, num in heap] #Extract the elements from the heap

        return top_k_elements