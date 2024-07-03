from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        list = [0 for i in range(1001)]
        for cit in citations:
            for j in range(cit+1):
                list[j] += 1

        ans = 0
        for i in range(1001):
            if list[i] >= i:
                ans = i

        return ans

sol = Solution()
print(sol.hIndex([3,0,6,1,5]))
