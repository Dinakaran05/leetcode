class Solution:
    def canConstruct(self, a: str, v: int) -> bool:
        if v > len(a): return False
        charCount = [0] * 26
        for c in a:
            charCount[ord(c) - ord('a')] += 1
        oddCount = 0
        for i in range(26):
            if charCount[i] % 2 == 1:
                oddCount += 1
        return oddCount <= v and v <= len(a)

            
        