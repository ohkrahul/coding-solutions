'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-18
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-18

## Problem Understanding and Approach

The problem asks us to implement the inorder traversal of a binary tree. Inorder traversal visits the nodes of a binary tree in the following order: left subtree, root, right subtree.

To solve this problem, we can use a recursive approach. We start at the root of the tree and recursively visit the left subtree, then visit the root, and finally visit the right subtree. This process is repeated for each node in the tree.

## Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node in the tree exactly once.

The space complexity of the inorder traversal is O(h), where h is the height of the tree. This is because the recursive calls can be stacked up to a maximum depth of h.

## Well-commented Implementation

```python
def inorder_traversal(root):
  """
  Performs an inorder traversal of a binary tree.

  Parameters:
    root: The root node of the binary tree.

  Returns:
    A list of the values in the binary tree in inorder.
  """

  # If the root is None, return an empty list.
  if root is None:
    return []

  # Recursively visit the left subtree.
  left_subtree = inorder_traversal(root.left)

  # Visit the root.
  root_value = root.val

  # Recursively visit the right subtree.
  right_subtree = inorder_traversal(root.right)

  # Return the list of values in inorder.
  return left_subtree + [root_value] + right_subtree
```

## Example Test Cases

```python
# Test case 1: A simple binary tree.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
result = inorder_traversal(root)
print(result)  # Output: [2, 1, 3]

# Test case 2: An empty binary tree.
root = None
result = inorder_traversal(root)
print(result)  # Output: []
```

## Alternative Approaches

An alternative approach to implementing the inorder traversal is to use a stack. We start at the root of the tree and push it onto the stack. Then, we recursively visit the left subtree of the current node. Once we reach the bottom of the left subtree, we pop the current node from the stack and visit it. We then recursively visit the right subtree of the current node. This process is repeated until there are no more nodes left on the stack.

The time and space complexity of the stack-based inorder traversal are the same as the recursive inorder traversal.

# Connect with me: https://github.com/ohkrahul
