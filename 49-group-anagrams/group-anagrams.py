class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            Understand
                - The idea is to find the words that are anagrams

                Questions
                    - Are we always guaranteed to have anagrams?
                    - Can we have an empty list?
                    - Are we always guaranteed to have a list with lowercase English letters?

            Match
                - Use dictionary
            
            Plan
                - Check if the list is empty
                    - Yes, return an empty array
                - Initialize a dictionary
                - Traverse through the list
                    - Sort the current word to use as a key
                    - Check if the key is in the dictionary
                        - Yes, append to the dictionary
                        - No, initialize
                - Return the values of the dictionary
        """
        if len(strs) == 0:
            return [[""]]
        
        dictionary = {}

        for word in strs:
            key ="".join(sorted(word))

            if key in dictionary:
                dictionary[key].append(word)
            else:
                dictionary[key] = [word]
        
        return dictionary.values()