class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        return " ".join(s)

'''
For python, this question can simply use split() to solve. 

The return line shows '" ".join(s) takes each element in the list s 
and concatenates them into a string, inserting a space (" ") between each element.

'''