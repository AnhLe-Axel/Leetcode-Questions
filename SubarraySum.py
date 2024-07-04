from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            target -= nums[i]
            res += 1
            if target <= 0:
                return res
        if target > 0:
            return 0
    
sol = Solution()
print(sol.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))