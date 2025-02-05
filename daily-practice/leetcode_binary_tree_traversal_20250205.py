'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-05
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-05

## Problem Understanding and Approach

Inorder traversal is a traversal technique for binary trees where the nodes are visited in the following order:

1. Recursively traverse the left subtree.
2. Visit the root node.
3. Recursively traverse the right subtree.

This traversal order produces a sorted list of the elements in the binary tree if the tree is a binary search tree (BST).

## Time and Space Complexity Analysis

The time complexity of the inorder traversal is `O(n)` where `n` is the number of nodes in the binary tree. This is because each node is visited exactly once.

The space complexity of the inorder traversal is `O(h)` where `h` is the height of the binary tree. This is because the recursive calls can potentially stack up to a depth of `h` in the worst case.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    """
    Performs an inorder traversal of a binary tree.

    Parameters:
    root: The root node of the binary tree.

    Returns:
    A list of the elements in the binary tree in inorder.
    """

    # If the root node is None, return an empty list.
    if root is None:
        return []

    # Recursively traverse the left subtree.
    left_subtree = inorder_traversal(root.left)

    # Visit the root node.
    root_value = root.val

    # Recursively traverse the right subtree.
    right_subtree = inorder_traversal(root.right)

    # Return the concatenation of the left subtree, root value, and right subtree.
    return left_subtree + [root_value] + right_subtree
```

## Example Test Cases

```python
# Test case 1: Empty tree
root = None
result = inorder_traversal(root)
print(result)  # Output: []

# Test case 2: Tree with one node
root = TreeNode(1)
result = inorder_traversal(root)
print(result)  # Output: [1]

# Test case 3: Tree with multiple nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
result = inorder_traversal(root)
print(result)  # Output: [2, 1, 3]
```

## Alternative Approaches

In some cases, it may be more efficient to use an iterative approach to perform an inorder traversal. The iterative approach uses a stack to keep track of the nodes that have been visited. The algorithm is as follows:

1. Push the root node onto the stack.
2. While the stack is not empty:
    1. Pop the top node from the stack.
    2. Visit the node.
    3. If the node has a right child, push the right child onto the stack.
    4. If the node has a left child, push the left child onto the stack.

The iterative approach has a time complexity of `O(n)` and a space complexity of `O(h)`, where `n` is the number of nodes in the binary tree and `h` is the height of the binary tree.

# Connect with me: https://github.com/ohkrahul
