'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-28
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-28

## Problem Understanding and Approach

The inorder traversal of a binary tree visits the left subtree, then the root, and then the right subtree.

To implement inorder traversal, we can use a recursive approach. The base case is when the root is null. In this case, we simply return. Otherwise, we recursively call inorder traversal on the left subtree, then visit the root, and then recursively call inorder traversal on the right subtree.

## Time and Space Complexity Analysis

The time complexity of inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node once.

The space complexity of inorder traversal is O(h), where h is the height of the tree. This is because we need to store the stack of nodes that we have visited but have not yet processed.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    """
    Performs inorder traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of the values in the binary tree in inorder.
    """

    # Base case: If the root is null, return an empty list.
    if root is None:
        return []

    # Recursively call inorder traversal on the left subtree.
    left_traversal = inorder_traversal(root.left)

    # Visit the root.
    root_value = root.val

    # Recursively call inorder traversal on the right subtree.
    right_traversal = inorder_traversal(root.right)

    # Return the concatenation of the left traversal, the root value, and the right traversal.
    return left_traversal + [root_value] + right_traversal
```

## Example Test Cases

```python
# Test case 1: A binary tree with three nodes.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(inorder_traversal(root))  # Output: [2, 1, 3]

# Test case 2: A binary tree with one node.
root = TreeNode(1)
print(inorder_traversal(root))  # Output: [1]

# Test case 3: A binary tree with no nodes.
root = None
print(inorder_traversal(root))  # Output: []
```

## Alternative Approaches

There are other ways to implement inorder traversal, such as using a stack or using Morris traversal. However, the recursive approach is the most straightforward and easiest to understand.

# Connect with me: https://github.com/ohkrahul
