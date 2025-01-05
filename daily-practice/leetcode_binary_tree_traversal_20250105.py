'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-05
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-05

## Problem Understanding and Approach

The inorder traversal of a binary tree refers to visiting the nodes of the tree in the following order:

1. Recursively visit the left subtree
2. Visit the current node
3. Recursively visit the right subtree

This type of traversal is commonly used for sorting the elements of a binary search tree.

## Time and Space Complexity Analysis

The time complexity of the inorder traversal is **O(n)**, where **n** is the number of nodes in the tree. This is because we need to visit every node once.

The space complexity is **O(n)** as well. This is because we need to store the recursive calls in the call stack, and the maximum number of recursive calls that can be made at any time is the height of the tree.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    """
    Perform an inorder traversal on a binary tree.

    Parameters:
        root: The root node of the binary tree.

    Returns:
        A list of the values of the nodes in the tree in inorder.
    """

    # If the root node is None, return an empty list.
    if root is None:
        return []

    # Create a list to store the values of the nodes in the tree.
    values = []

    # Recursively visit the left subtree.
    values.extend(inorder_traversal(root.left))

    # Visit the current node.
    values.append(root.val)

    # Recursively visit the right subtree.
    values.extend(inorder_traversal(root.right))

    # Return the list of values.
    return values
```

## Example Test Cases

```python
# Create a binary tree.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Perform an inorder traversal on the tree.
values = inorder_traversal(root)

# Print the values of the nodes in the tree.
print(values)  # Output: [2, 1, 3]
```

## Alternative Approaches

An alternative approach to performing an inorder traversal is to use a stack. The algorithm for this approach is as follows:

1. Initialize a stack with the root node.
2. While the stack is not empty, do the following:
    1. Pop the top node from the stack.
    2. Visit the node.
    3. If the node has a right child, push the right child onto the stack.
    4. If the node has a left child, push the left child onto the stack.

This approach has the same time and space complexity as the recursive approach.

# Connect with me: https://github.com/ohkrahul
