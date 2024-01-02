class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                l.append(s[i])  ## extract all vowels from the input list
                s[i]="*"    ## vowel characters are replaced by *
        l = l[::1]  ## This reverses the list l
        start = 0
        for i in range(len(s)):
            if s[i] == "*" and start <len(l):
                s[i] = l[start]
                start+=1
        str1=""
        for i in s:
            str1+=i #Reconstruct the string
        return str1