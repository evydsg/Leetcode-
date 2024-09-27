"""
    Understand: the idea is to reverse the order of the words
        - Can the string be empty?
        - Can we get other characters than lower case letters?

    Match
        Two Pointers
    
    Plan
        Convert the string into a list, splitting by space
        Initialize two pointers: left and right
        Iterate through the list as long as left and right have not meet
        Swap
        Convert the list into a string





"""
class Solution:
    def reverseWords(self, s: str) -> str:
        listWords = s.split()
        left, right = 0, len(listWords)-1

        while left < right:
            listWords[left], listWords[right] = listWords[right], listWords[left]

            left += 1
            right -= 1
        
        return " ".join(listWords)

        