from typing import List
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def addValue(self, value):
        if self.value >= value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.addValue(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.addValue(value)
    
class Tree:
    def __init__(self,):
        self.root = None
    
    def addValue(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.addValue(value)

    def traverse(self):
        queue = []
        nums = list()
        # Traverse the tree
        if self.root is not None:
            queue.append(self.root)
        while(len(queue) != 0):
            node = queue.pop(0)
            nums.append(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return nums

class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        tree = Tree()
        index = math.floor(len(nums) / 2)
        tree.addValue(nums[index])
        del nums[index]
        for i in nums:
            tree.addValue(i)
        return tree.traverse()
        

sol = Solution()
print(sol.sortedArrayToBST([-10,-3,0,5,9]))