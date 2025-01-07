class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        result = []

        for i in range(n):
            for j in range(n):
                if i != j and words[j].find(words[i]) != -1:
                    result.append(words[i])
                    break

        return result
        