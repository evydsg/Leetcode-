"""
    Understand: the idea is to write an algorithm that converts a list into a string and converts it back to a list
                - Can the list be empty?
                - Can the list have any other characters than letters?

    Match
        Arrays & Hashin
    
    Plan
        - Encode
            Iterate through the list
            Append the current length, delimiter and the word into the string
            Return the string
        
        - Decode
            Initialize a list
            Iterate through the list using a pointer
            Initialize a second pointer
                Use the second pointer to get the length
            Get the word
                From the second pointer + 1:
                append it to the list
                move pointer

        
        




"""

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        
        return string
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        index = 0

        while index < len(s):
            length = ""
            second = index

            while s[second] != "#":
                length += s[second]
                second += 1
            
            length = int(length) + second + 1
            result.append( s[second + 1: length])

            index = length
        
        return result





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))