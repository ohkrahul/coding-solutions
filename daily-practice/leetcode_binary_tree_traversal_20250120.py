'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-20
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-20

### Problem Understanding

The inorder traversal of a binary tree involves visiting the nodes of the tree in the following order: left subtree, root, and right subtree. This traversal is often used to print the elements of the tree in ascending order.

### Approach

To perform inorder traversal, we can use a recursive algorithm that traverses the binary tree as follows:

1. If the current node is not null,
2. Traverse the left subtree using the inorder traversal algorithm.
3. Visit the current node.
4. Traverse the right subtree using the inorder traversal algorithm.

### Implementation

```python
def inorder_traversal(root):
  """
  Performs inorder traversal of a binary tree.

  Args:
    root: The root node of the binary tree.

  Returns:
    A list of the elements of the binary tree in inorder.
  """

  # If the root is null, return an empty list.
  if root is None:
    return []

  # Recursively traverse the left subtree.
  left_subtree = inorder_traversal(root.left)

  # Add the current node to the list.
  left_subtree.append(root.val)

  # Recursively traverse the right subtree.
  right_subtree = inorder_traversal(root.right)

  # Return the concatenated list of the left subtree, root, and right subtree.
  return left_subtree + right_subtree
```

### Time and Space Complexity Analysis

The time complexity of the inorder traversal algorithm is O(n), where n is the number of nodes in the binary tree. This is because the algorithm visits each node in the tree exactly once.

The space complexity of the inorder traversal algorithm is O(n), where n is the number of nodes in the binary tree. This is because the algorithm uses a stack to store the nodes that have been visited but not yet processed.

### Example Test Cases

```python
# Example 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(inorder_traversal(root))  # Output: [2, 1, 3]

# Example 2:
root = TreeNode(1)
root.right = TreeNode(2)
print(inorder_traversal(root))  # Output: [1, 2]

# Example 3:
root = None
print(inorder_traversal(root))  # Output: []
```

### Alternative Approaches

There are several alternative approaches to performing inorder traversal of a binary tree. One approach is to use a stack. The stack is initially empty. The algorithm then performs the following steps:

1. While the current node is not null,
2. Push the current node onto the stack.
3. Set the current node to the left child of the current node.
4. If the current node is null,
5. Pop the top node from the stack and visit it.
6. Set the current node to the right child of the popped node.

Another approach to performing inorder traversal of a binary tree is to use Morris traversal. Morris traversal does not require the use of a stack or recursion. Instead, it uses a pointer to traverse the tree. The algorithm then performs the following steps:

1. Initialize the current node to the root node.
2. While the current node is not null,
3. If the left child of the current node is null,
4. Visit the current node.
5. Set the current node to the right child of the current node.
6. Otherwise,
7. Find the inorder predecessor of the current node.
8. Set the right child of the inorder predecessor to the current node.
9. Set the current node to the left child of the current node.
10. Set the right child of the inorder predecessor to null.

# Connect with me: https://github.com/ohkrahul
