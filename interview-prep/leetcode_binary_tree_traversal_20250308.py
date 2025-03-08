'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-03-08
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-03-08

```python
"""
Problem: Binary Tree Inorder Traversal (LeetCode #94)
Difficulty: Easy

Description:
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Inorder traversal visits the left subtree, then the root, then the right subtree.

Example:
Input: root = [1,null,2,3]
Output: [1,3,2]
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an inorder traversal of a binary tree.

        Args:
            root: The root of the binary tree.

        Returns:
            A list containing the inorder traversal of the tree's values.
        """

        result = []

        # Recursive helper function
        def inorder(node):
            if node:
                inorder(node.left)  # Traverse left subtree
                result.append(node.val)  # Visit root
                inorder(node.right) # Traverse right subtree

        inorder(root)
        return result


    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an inorder traversal iteratively using a stack.

        Args:
            root: The root of the binary tree.

        Returns:
            A list containing the inorder traversal of the tree's values.
        """
        result = []
        stack = []
        curr = root

        while curr or stack:
            while curr:  # Go left as far as possible
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()  # Process the node
            result.append(curr.val)
            curr = curr.right   # Explore the right subtree

        return result



# Example Test Cases
root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))  # Example from the problem description
root2 = None  # Empty tree
root3 = TreeNode(1)  # Single node tree
root4 = TreeNode(1, TreeNode(2), TreeNode(3)) # Balanced Tree


solution = Solution()
print(f"Test Case 1: {solution.inorderTraversal(root1)}")  # Output: [1, 3, 2]
print(f"Test Case 2: {solution.inorderTraversal(root2)}")  # Output: []
print(f"Test Case 3: {solution.inorderTraversal(root3)}")  # Output: [1]
print(f"Test Case 4: {solution.inorderTraversal(root4)}")  # Output: [2, 1, 3]


print(f"Test Case 1 (Iterative): {solution.inorderTraversal_iterative(root1)}")  # Output: [1, 3, 2]
print(f"Test Case 2 (Iterative): {solution.inorderTraversal_iterative(root2)}")  # Output: []
print(f"Test Case 3 (Iterative): {solution.inorderTraversal_iterative(root3)}")  # Output: [1]
print(f"Test Case 4 (Iterative): {solution.inorderTraversal_iterative(root4)}")  # Output: [2, 1, 3]



"""
Time and Space Complexity Analysis:

Recursive Approach:
- Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
- Space Complexity: O(H) in the worst case (skewed tree) due to the recursion stack, where H is the height of the tree. 
  In the average case (balanced tree), the space complexity is O(log N).

Iterative Approach:
- Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
- Space Complexity: O(H) in the worst case (skewed tree) due to the stack, where H is the height of the tree. 
  In the average case (balanced tree), the space complexity is O(log N).

Alternative Approaches:
- Morris Traversal: An inorder traversal algorithm that uses threaded binary trees to achieve O(N) time complexity and O(1) space complexity.  More complex to implement.
"""


```

# Connect with me: https://github.com/ohkrahul
