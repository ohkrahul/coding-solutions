'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-03
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-03

## Problem Understanding and Approach

The inorder traversal of a binary tree visits the nodes in the following order: left subtree, root, right subtree.

To perform inorder traversal recursively, we can follow these steps:

1. If the left subtree is not empty, traverse it recursively.
2. Visit the root node.
3. If the right subtree is not empty, traverse it recursively.

## Time and Space Complexity Analysis

The time complexity of inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node once.

The space complexity of inorder traversal is O(h), where h is the height of the tree. This is because we store the call stack during recursion.

### Well-Commented Implementation

```python
def inorder_traversal(root):
  """
  Performs inorder traversal of a binary tree.

  Parameters:
    root: The root node of the tree.

  Returns:
    A list of the values of the nodes in the tree, in inorder.
  """

  # If the tree is empty, return an empty list.
  if not root:
    return []

  # Recursively traverse the left subtree.
  left_subtree = inorder_traversal(root.left)

  # Visit the root node.
  root_value = root.val

  # Recursively traverse the right subtree.
  right_subtree = inorder_traversal(root.right)

  # Return the values of the nodes in the tree, in inorder.
  return left_subtree + [root_value] + right_subtree
```

### Example Test Cases

```python
# Test case 1: Empty tree.
root = None
result = inorder_traversal(root)
print(result)  # []

# Test case 2: Tree with one node.
root = TreeNode(1)
result = inorder_traversal(root)
print(result)  # [1]

# Test case 3: Tree with multiple nodes.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
result = inorder_traversal(root)
print(result)  # [2, 1, 3]
```

### Alternative Approaches

In addition to the recursive approach, there is also an iterative approach to inorder traversal. The iterative approach uses a stack to keep track of the nodes that have been visited.

The iterative approach has the same time and space complexity as the recursive approach. However, the iterative approach is often preferred because it is easier to implement and does not require the use of recursion.

# Connect with me: https://github.com/ohkrahul
