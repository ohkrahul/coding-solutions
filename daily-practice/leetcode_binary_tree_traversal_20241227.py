'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-27
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-27

## Problem Understanding and Approach

The inorder traversal of a binary tree involves visiting the nodes in the following order: left subtree, root node, right subtree.

We can use a recursive approach to implement inorder traversal. The base case is when the root node is null, in which case we simply return. Otherwise, we first recursively traverse the left subtree, then visit the root node, and finally, recursively traverse the right subtree.

## Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node exactly once.

The space complexity of the inorder traversal is O(h), where h is the height of the tree. This is because the recursion stack can be as deep as the height of the tree.

## Well-commented Implementation

```python
def inorder_traversal(root):
    if root is None:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
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

# Inorder traversal of the binary tree
print(inorder_traversal(tree))  # Output: [2, 1, 3]
```

## Alternative Approaches

An alternative approach to inorder traversal is to use a stack. We start by pushing the root node onto the stack. Then, while the stack is not empty, we pop the top node from the stack, visit the node, and push its right child onto the stack. We repeat this process until the stack is empty.

# Connect with me: https://github.com/ohkrahul
