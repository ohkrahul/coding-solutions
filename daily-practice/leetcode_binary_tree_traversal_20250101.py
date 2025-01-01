'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-01
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-01

## Problem Understanding and Approach

The inorder traversal of a binary tree requires visiting the left subtree, the root, and the right subtree in that order. We can implement this using recursion or a stack-based iterative approach.

## Time and Space Complexity Analysis

* **Time complexity:** O(N), where N is the number of nodes in the tree. This is because we visit each node exactly once.
* **Space complexity:** O(N) for the recursive approach (due to the stack frames) and O(1) for the iterative approach.

## Well-Commented Implementation (Recursive)

```python
"""
Definition for a binary tree node.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Perform inorder traversal of a binary tree.
        
        :param root: The root node of the tree.
        :return: A list of the values visited in inorder.
        """
        
        # Recursively traverse the left subtree
        if root.left:
            left_subtree_values = self.inorderTraversal(root.left)
        else:
            left_subtree_values = []
        
        # Append the root's value to the list
        left_subtree_values.append(root.val)
        
        # Recursively traverse the right subtree
        if root.right:
            right_subtree_values = self.inorderTraversal(root.right)
        else:
            right_subtree_values = []
        
        # Return the concatenated list of values
        return left_subtree_values + right_subtree_values
```

## Example Test Cases

```python
# Test case 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
output = [2, 1, 3]
assert Solution().inorderTraversal(root) == output

# Test case 2:
root = TreeNode(1)
root.right = TreeNode(2)
output = [1, 2]
assert Solution().inorderTraversal(root) == output

# Test case 3:
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
output = [3, 2, 1, 4, 5]
assert Solution().inorderTraversal(root) == output
```

## Alternative Approaches (Iterative)

An iterative approach using a stack can also be used to implement inorder traversal. The idea is to push the root node into the stack and then repeatedly pop the top element of the stack, visit it, and push its right (and then left) child into the stack until the stack is empty.

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        current = root
        
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right
                
        return result
```

# Connect with me: https://github.com/ohkrahul
