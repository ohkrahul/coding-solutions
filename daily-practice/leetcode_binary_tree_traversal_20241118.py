'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-18
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-18

## 1. Problem Understanding and Approach

The inorder traversal of a binary tree visits the nodes in the order left, root, right. To implement this traversal, we can use a recursive approach. The base case is when the tree is empty. Otherwise, we first traverse the left subtree, then visit the root, and finally traverse the right subtree.

## 2. Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node once. The space complexity is O(h), where h is the height of the tree. This is because we need to store the recursion stack, which has a maximum depth of h.

## 3. Well-Commented Implementation

```python
def inorder_traversal(root):
  """
  Perform inorder traversal of a binary tree.

  Parameters:
    root: The root node of the binary tree.

  Returns:
    A list of the values of the nodes in the tree, in inorder.
  """

  # Base case: Empty tree.
  if root is None:
    return []

  # Recursively traverse the left subtree.
  left_traversal = inorder_traversal(root.left)

  # Visit the root.
  root_value = root.val

  # Recursively traverse the right subtree.
  right_traversal = inorder_traversal(root.right)

  # Return the concatenation of the left, root, and right traversals.
  return left_traversal + [root_value] + right_traversal
```

## 4. Example Test Cases

```python
# Test case 1: Empty tree.
root = None
assert inorder_traversal(root) == []

# Test case 2: Tree with one node.
root = TreeNode(1)
assert inorder_traversal(root) == [1]

# Test case 3: Tree with multiple nodes.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert inorder_traversal(root) == [2, 1, 3]
```

## 5. Alternative Approaches

There are several other ways to implement inorder traversal of a binary tree. Here are two common alternatives:

1. **Iterative approach:** This approach uses a stack to keep track of the nodes that have been visited. We start by pushing the root node onto the stack. Then, while the stack is not empty, we pop the top node from the stack and visit it. If the node has a right child, we push the right child onto the stack. If the node has a left child, we push the left child onto the stack.

2. **Morris traversal:** This approach uses a pointer to keep track of the current node. We start by setting the pointer to the root node. Then, while the pointer is not None, we check if the node has a left child. If it does, we find the inorder predecessor of the node and set the pointer to the inorder predecessor. Otherwise, we visit the node and set the pointer to the right child of the node.

# Connect with me: https://github.com/ohkrahul
