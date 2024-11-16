'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-15
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-15

## Problem Understanding and Approach

Inorder traversal of a binary tree involves visiting the nodes of the tree in the following order: left subtree, root, right subtree. This traversal is often used to obtain the nodes of the tree in sorted order.

Our approach is to use recursion to traverse the binary tree. We will define a recursive function that takes the root node of a subtree as its argument. The function will visit the left subtree, then the root node, and finally the right subtree. The function will be called on each subtree until the entire tree has been traversed.

## Time and Space Complexity Analysis

The time complexity of an inorder traversal is O(n), where n is the number of nodes in the binary tree. This is because each node in the tree is visited exactly once. The space complexity is also O(n), because the recursion stack can contain up to n nodes at any given time.

## Well-Commented Implementation

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # If the root node is None, return an empty list.
        if root is None:
            return []

        # Recursively traverse the left subtree.
        left_subtree = self.inorderTraversal(root.left)

        # Add the root node's value to the list.
        left_subtree.append(root.val)

        # Recursively traverse the right subtree.
        right_subtree = self.inorderTraversal(root.right)

        # Return the concatenated list of the left subtree, root node, and right subtree.
        return left_subtree + right_subtree
```

## Example Test Cases

```python
# Example 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
result = Solution().inorderTraversal(root)
print(result)  # [2, 1, 3]

# Example 2:
root = TreeNode(1)
result = Solution().inorderTraversal(root)
print(result)  # [1]

# Example 3:
root = None
result = Solution().inorderTraversal(root)
print(result)  # []
```

## Alternative Approaches

There are other ways to perform an inorder traversal of a binary tree. One alternative approach is to use a stack. The stack is used to store the nodes that have been visited but not yet processed. The algorithm starts by pushing the root node onto the stack. Then, while the stack is not empty, the following steps are performed:

1. Pop the top node from the stack.
2. Visit the node.
3. Push the node's right child onto the stack.
4. Push the node's left child onto the stack.

This algorithm will visit the nodes of the tree in the following order: left subtree, root, right subtree.

# Connect with me: https://github.com/ohkrahul
