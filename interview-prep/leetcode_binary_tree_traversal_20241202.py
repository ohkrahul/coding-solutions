'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-02
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-02

## Problem Understanding and Approach

The inorder traversal of a binary tree involves visiting the nodes in the following order: left subtree, root, and right subtree. This can be achieved recursively by first traversing the left subtree, then processing the current root, and finally traversing the right subtree. The result is a sorted list of the values present in the tree.

## Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the tree. This is because each node is visited once during the traversal.

The space complexity of the inorder traversal is O(h), where h is the height of the tree. This is because the recursive calls can stack up to a depth of h.

## Well-commented Implementation

```python
def inorder_traversal(root):
  """
  Performs inorder traversal of a binary tree.

  Args:
    root: The root node of the binary tree.

  Returns:
    A list of the values in the binary tree in inorder.
  """

  # If the root is None, return an empty list.
  if root is None:
    return []

  # Recursively traverse the left subtree.
  left_traversal = inorder_traversal(root.left)

  # Append the root's value to the list.
  left_traversal.append(root.val)

  # Recursively traverse the right subtree.
  right_traversal = inorder_traversal(root.right)

  # Return the concatenation of the left and right traversals.
  return left_traversal + right_traversal
```

## Example Test Cases

```python
# Test case 1: Empty tree.
root = None
assert inorder_traversal(root) == []

# Test case 2: Single-node tree.
root = TreeNode(1)
assert inorder_traversal(root) == [1]

# Test case 3: Binary tree.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert inorder_traversal(root) == [2, 1, 3]
```

## Alternative Approaches

In addition to the recursive approach presented above, there are other ways to perform inorder traversal of a binary tree:

* **Iterative approach:** This approach uses a stack to keep track of the nodes that have been visited. The algorithm starts at the root node and pushes it onto the stack. Then, while the stack is not empty, the top node is popped and its value is added to the result list. The algorithm then pushes the left and right children of the popped node onto the stack, and continues until the stack is empty.
* **Morris traversal:** This approach uses a pointer to keep track of the current node. The algorithm starts at the root node and moves to its left child. If the left child is None, the algorithm prints the current node's value and moves to its right child. If the left child is not None, the algorithm finds the inorder predecessor of the current node, which is the rightmost node in the current node's left subtree. The algorithm then makes the inorder predecessor's right child point to the current node, and moves to the inorder predecessor. This process is repeated until the algorithm reaches the root node again.

# Connect with me: https://github.com/ohkrahul
