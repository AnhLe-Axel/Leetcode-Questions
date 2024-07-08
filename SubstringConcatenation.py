from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass
    
    def isConcatenation(self, s: str, words: List[str]) -> bool:
        n = len(words[0])
        length = n * len(words)
        word_set = set(words)
        res = True

        if len(s) == length:
            for i in range(len(words)):
                word = s[i*n:i*n+n]
                if word in word_set:
                    word_set.remove(word)
                else:
                    res = False
                    break
        else:
            res = False
        return res

sol = Solution()
print(sol.isConcatenation("barhoofoo", ["foo","bar", "the"]))
