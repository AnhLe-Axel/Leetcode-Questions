from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indexes = []
        counts = dict()
        n = len(s)
        num = len(words)
        word_len = len(words[0])

        if (n < num):
            return indexes

        for word in words:
            if word not in counts:
                counts[word] = 0            
            counts[word] += 1

        for i in range(0, n - num*word_len + 1, 1):
            temp_counts = dict()
            j = 0
            while(j < num):
                substring = s[i + j*word_len:i + (j+1) *word_len]
                if substring not in counts:
                    break
                if substring not in temp_counts:
                    temp_counts[substring] = 0
                temp_counts[substring] += 1
                if temp_counts[substring] > counts[substring]:
                    break
                j += 1
            if j == num:
                indexes.append(i)

        return indexes

sol = Solution()
print(sol.findSubstring("barfoothefoobarman", ["foo","bar"]))