class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            Understand
                The idea is to find the anagrams and group them all together

                Can we have a list with no anagrams?
                Are we always guaranteed to receive lowercase letters?
                Can we receive an empty list?
            
            Match
                Dictionary 
            
            Plan
                Initialize a dictionary
                Iterate through the list
                    Sort each word to use it as the key
                        Check if the key already exists in the dictionary
                    Add the key to the dictionary
                Return the values of the dictionary as a list
            
            Evaluate
                Time Complexity: O(n)
                Space Complexity: O(n)
        """
        dictionary = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in dictionary:
                dictionary[key].append(word)
            else:
                dictionary[key] = [word]
        
        return list(dictionary.values())