from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indexes = []
        counts = dict()
        n = len(s)
        num = len(words)
        word_len = len(words[0])

        if n < num:
            return indexes

        for word in words:
            if word not in counts:
                counts[word] = 0
            counts[word] += 1

        for i in range(0, n - num * word_len + 1, 1):
            temp_counts = dict()
            word_used = 0

            for j in range(i, i + num * word_len, word_len):
                substring = s[j: j + word_len]
                if substring not in counts:
                    break
                if substring not in temp_counts:
                    temp_counts[substring] = 0
                temp_counts[substring] += 1
                if temp_counts[substring] > counts[substring]:
                    break
                word_used += 1

            if word_used == num:
                indexes.append(i)

        return indexes


sol = Solution()
print(sol.findSubstring("barfoofoobarthefoobarman", ["foo","bar", "the"]))