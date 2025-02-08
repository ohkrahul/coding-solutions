'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-08
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-08

## Problem Understanding and Approach

The inorder traversal of a binary tree visits the nodes of the tree in the following order: left subtree, root, right subtree.

We can implement this traversal using a recursive algorithm. The algorithm will take as input the root node of the tree and will perform the following steps:

1. If the root node is not null, then
   - Recursively traverse the left subtree.
   - Visit the root node.
   - Recursively traverse the right subtree.

## Time and Space Complexity Analysis

The time complexity of the inorder traversal algorithm is O(n), where n is the number of nodes in the tree. This is because the algorithm visits each node in the tree exactly once.

The space complexity of the algorithm is O(h), where h is the height of the tree. This is because the algorithm uses a stack to store the nodes that have been visited but have not yet been processed. The height of the tree is the maximum number of nodes on a path from the root to a leaf.

## Well-commented Implementation

```python
def inorder_traversal(root):
  """
  Performs an inorder traversal of a binary tree.

  Parameters:
    root: The root node of the tree.

  Returns:
    A list of the values of the nodes in the tree in inorder.
  """

  # If the root node is null, then return an empty list.
  if root is None:
    return []

  # Create a list to store the values of the nodes in the tree.
  values = []

  # Recursively traverse the left subtree.
  values.extend(inorder_traversal(root.left))

  # Visit the root node.
  values.append(root.val)

  # Recursively traverse the right subtree.
  values.extend(inorder_traversal(root.right))

  # Return the list of values.
  return values
```

## Example Test Cases

The following are some example test cases for the inorder_traversal function:

```python
# Test case 1: An empty tree.
root = None
assert inorder_traversal(root) == []

# Test case 2: A tree with one node.
root = TreeNode(1)
assert inorder_traversal(root) == [1]

# Test case 3: A tree with two nodes.
root = TreeNode(1)
root.right = TreeNode(2)
assert inorder_traversal(root) == [1, 2]

# Test case 4: A tree with three nodes.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert inorder_traversal(root) == [2, 1, 3]

# Test case 5: A tree with four nodes.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
assert inorder_traversal(root) == [2, 1, 3, 4]
```

## Alternative Approaches

There are several other ways to implement the inorder traversal of a binary tree. One alternative approach is to use a stack. The algorithm will take as input the root node of the tree and will perform the following steps:

1. Push the root node onto the stack.
2. While the stack is not empty,
   - Pop the top node from the stack.
   - Visit the node.
   - Push the node's right child onto the stack.
   - Push the node's left child onto the stack.

This approach has the same time and space complexity as the recursive approach.

# Connect with me: https://github.com/ohkrahul
