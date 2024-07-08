from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        if len(s) == 0:
            return 0
        for i in range(len(s)-1):
            count = 1
            for j in range(i + 1, len(s)):
                if s[j] in s[i:j]:
                    if count > max: 
                        max = count
                        break
                else:
                    count += 1
        return max

sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))