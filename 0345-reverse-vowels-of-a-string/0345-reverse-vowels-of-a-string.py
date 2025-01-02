class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r=0,len(s)-1
        word=list(s)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        while l<r:
            while l<r and word[l] not in vowels:
                l+=1
            while l<r and word[r] not in vowels:
                r-=1
            word[l],word[r]=word[r],word[l]
            l+=1
            r-=1
        return "".join(word)
            