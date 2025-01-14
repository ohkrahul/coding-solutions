'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-14
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-14

## Problem Understanding and Approach

### Problem Understanding

Inorder traversal of a binary tree involves visiting the nodes in the following order:

1. Traverse the left subtree.
2. Visit the root node.
3. Traverse the right subtree.

### Approach

We will use a recursive approach to traverse the binary tree in inorder. The function will take the root node as its input and perform the following steps:

1. If the root node is not null,
    - Recursively call the function on the root's left child.
    - Visit the root node.
    - Recursively call the function on the root's right child.

## Time and Space Complexity Analysis

### Time Complexity

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node exactly once.

### Space Complexity

The space complexity of the inorder traversal is O(h), where h is the height of the tree. This is because the recursive calls can form a stack of height h.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    """
    Perform an inorder traversal of a binary tree.

    Args:
    root: The root node of the binary tree.

    Returns:
    A list of the values of the nodes in the tree in inorder.
    """

    # If the root node is null, return an empty list.
    if root is None:
        return []

    # Recursively call the function on the root's left child.
    left_values = inorder_traversal(root.left)

    # Visit the root node.
    root_value = root.val

    # Recursively call the function on the root's right child.
    right_values = inorder_traversal(root.right)

    # Return the values of the nodes in the tree in inorder.
    return left_values + [root_value] + right_values
```

## Example Test Cases

```python
# Test case 1: Empty tree
root = None
assert inorder_traversal(root) == []

# Test case 2: Tree with one node
root = TreeNode(1)
assert inorder_traversal(root) == [1]

# Test case 3: Tree with multiple nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
assert inorder_traversal(root) == [2, 1, 3]
```

## Alternative Approaches

There are several other ways to traverse a binary tree in inorder. One alternative approach is to use a stack. We can push the root node onto the stack and then while the stack is not empty, we pop the top node off the stack, visit it, and push its right and left children onto the stack.

Another alternative approach is to use a Morris traversal. This approach does not use recursion or a stack, but it does require modifying the tree. The idea is to find the inorder predecessor of each node and then use this predecessor to visit the node.

# Connect with me: https://github.com/ohkrahul
