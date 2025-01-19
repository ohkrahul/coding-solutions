'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-19
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-19

## Problem Understanding and Approach

**Problem Statement:** Implement inorder traversal of a binary tree. Inorder traversal visits the left subtree, the root, and then the right subtree.

**Approach:** The problem can be solved using a recursive approach. The `inorder` function will take a root node as an argument. If the root is `None`, the function will return. Otherwise, it will call itself on the left subtree, print the value of the root, and call itself on the right subtree.

## Time and Space Complexity Analysis

**Time Complexity:** O(n), where n is the number of nodes in the tree.

**Space Complexity:** O(h), where h is the height of the tree.

## Well-Commented Implementation

```python
def inorder(root):
  """
  Performs inorder traversal of a binary tree.

  Parameters:
    root: The root node of the tree.

  Returns:
    None
  """

  # If the root is None, return
  if root is None:
    return

  # Recursively call inorder on the left subtree
  inorder(root.left)

  # Print the value of the root
  print(root.val)

  # Recursively call inorder on the right subtree
  inorder(root.right)
```

## Example Test Cases

**Example 1:**

```
Input:
    1
   / \
  2   3

Output:
2 1 3
```

**Example 2:**

```
Input:
      5
     / \
    3   7
   / \   \
  2   4   9

Output:
2 3 4 5 7 9
```

## Alternative Approaches

**Iterative Approach:** An iterative approach can also be used to implement inorder traversal. This approach uses a stack to keep track of the nodes that have been visited. The following code demonstrates the iterative approach:

```python
def inorder_iterative(root):
  """
  Performs inorder traversal of a binary tree iteratively.

  Parameters:
    root: The root node of the tree.

  Returns:
    None
  """

  # Create a stack to store the nodes
  stack = []

  # Push the root node onto the stack
  stack.append(root)

  # While the stack is not empty
  while stack:

    # Pop the top node from the stack
    node = stack.pop()

    # If the node is not None
    if node is not None:

      # Print the value of the node
      print(node.val)

      # Push the right child of the node onto the stack
      stack.append(node.right)

      # Push the left child of the node onto the stack
      stack.append(node.left)
```

# Connect with me: https://github.com/ohkrahul
