from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = -1
        right = -1
        rain = 0
        for i in range(n):
            if left == -1:
                if height[i] > 0:
                    left = i
            if right == -1:
                if height[i] > 0:
                    right = i
            if height[i] >= height[left]:
                right = i
                rain += self.cal_rain_between(left, right, height)
                left = right
        while self.find_max_index_after(left+1, height) > 0:
            right = self.find_max_index_after(left+1, height)
            rain += self.cal_rain_between(left, right, height)
            left = right

        return rain
    
    def cal_rain_between(self, left: int, right: int, height: List[int])-> int:
        rain = 0
        depth = min(height[left], height[right])
        for i in range(left, right):
            rain += max(0, depth - height[i])
        return rain
    
    def find_max_index_after(self, start, height: List[int]) -> int:
        index = -1
        max = 0
        if start < len(height):
            for i in range(start, len(height)):
                if height[i] > max:
                    max = height[i]
                    index = i
        return index


sol = Solution()
print(sol.trap([4,2,0,3,2,5]))