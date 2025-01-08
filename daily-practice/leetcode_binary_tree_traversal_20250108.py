'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-08
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-08

## Problem Understanding and Approach

### Problem Understanding

Given the root node of a binary tree, the goal is to perform an inorder traversal of the tree and return a list of the values stored in the nodes in the order they were visited during the traversal.

### Approach

Inorder traversal involves visiting the left subtree recursively, then the root, and finally the right subtree recursively. This approach can be implemented using a recursive algorithm or a stack-based iterative algorithm.

## Time and Space Complexity Analysis

### Time Complexity: O(N)

The algorithm visits each node exactly once. There are a total of N nodes in the tree, so the time complexity is O(N).

### Space Complexity: O(N)

In the worst case, the algorithm can use up to O(N) space in the stack to keep track of recursive calls. This happens when the tree is skewed, and the recursion goes deep into one side of the tree.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    # Recursive implementation of inorder traversal
    
    # Base case: If the root is None, return an empty list
    if root is None:
        return []
    
    # Recursively traverse the left subtree
    left_subtree = inorder_traversal(root.left)
    
    # Visit the root node
    value = root.val
    
    # Recursively traverse the right subtree
    right_subtree = inorder_traversal(root.right)
    
    # Combine the results of the left and right subtree traversals
    return left_subtree + [value] + right_subtree
```

## Example Test Cases

```python
# Example binary tree
tree = {
    "val": 1,
    "left": {
        "val": 2,
        "left": None,
        "right": None
    },
    "right": {
        "val": 3,
        "left": None,
        "right": None
    }
}

# Perform inorder traversal and print the result
result = inorder_traversal(tree)
print(result)  # Output: [2, 1, 3]

# Test case for empty tree
empty_tree = None
result = inorder_traversal(empty_tree)
print(result)  # Output: []
```

## Alternative Approaches

### Iterative Approach

The inorder traversal can also be implemented iteratively using a stack. The algorithm is as follows:

1. Initialize a stack and push the root node onto the stack.
2. While the stack is not empty:
    - Pop the top node from the stack.
    - Visit the node.
    - Push the right child of the node onto the stack.
    - Push the left child of the node onto the stack.

This iterative approach has the same time and space complexity as the recursive approach.

# Connect with me: https://github.com/ohkrahul
