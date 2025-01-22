'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-22
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-22

## 1. Problem Understanding and Approach

The inorder traversal of a binary tree visits the nodes in the following order:

1. Traverse the left subtree in order.
2. Visit the root.
3. Traverse the right subtree in order.

We can implement this algorithm recursively by first calling the inorder traversal on the left subtree, then visiting the root, and finally calling the inorder traversal on the right subtree.

## 2. Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the tree. This is because each node is visited exactly once.

The space complexity of the inorder traversal is O(h), where h is the height of the tree. This is because the recursive calls can be stacked up to a maximum depth of h.

## 3. Well-commented Implementation

```python
def inorder_traversal(root):
  """
  Perform an inorder traversal of a binary tree.

  Parameters:
    root: The root node of the binary tree.

  Returns:
    A list of the values of the nodes in the tree, in inorder.
  """

  # If the root is None, return an empty list.
  if root is None:
    return []

  # Recursively traverse the left subtree.
  left_traversal = inorder_traversal(root.left)

  # Visit the root.
  root_value = root.val

  # Recursively traverse the right subtree.
  right_traversal = inorder_traversal(root.right)

  # Return the concatenation of the left traversal, the root value, and the right traversal.
  return left_traversal + [root_value] + right_traversal
```

## 4. Example Test Cases

```python
# Test case 1: Empty tree.
root = None
result = inorder_traversal(root)
assert result == []

# Test case 2: Tree with one node.
root = TreeNode(1)
result = inorder_traversal(root)
assert result == [1]

# Test case 3: Tree with multiple nodes.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
result = inorder_traversal(root)
assert result == [2, 1, 3]
```

## 5. Alternative Approaches

There are several alternative approaches to performing an inorder traversal of a binary tree. One approach is to use a stack. We can start by pushing the root node onto the stack. Then, while the stack is not empty, we can pop the top node from the stack, visit it, and push its right child onto the stack. Finally, we can push its left child onto the stack. This process will continue until the stack is empty, and we will have visited all the nodes in the tree in inorder.

Another approach to performing an inorder traversal of a binary tree is to use a Morris traversal. This traversal does not require the use of a stack or recursion. Instead, we start at the root node and keep track of the previous node that we visited. If the current node has no left child, we visit it and move to its right child. If the current node has a left child, we find the rightmost node in its left subtree and make it the right child of the previous node. Then, we visit the current node and move to its left child. This process continues until we have visited all the nodes in the tree in inorder.

# Connect with me: https://github.com/ohkrahul
