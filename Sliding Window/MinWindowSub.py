from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        
        left = 0
        right = 0
        str_count = Counter(t)
        required = len(str_count)
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None

        while right < len(s):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in str_count and window_counts[character] == str_count[character]:
                formed += 1
            while left <= right and formed == required:
                character = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_counts[character] -= 1
                if character in str_count and window_counts[character] < str_count[character]:
                    formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))