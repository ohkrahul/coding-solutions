'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-26
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-26

## Problem Understanding and Approach

Given a binary tree, the task is to perform inorder traversal on it. Inorder traversal visits the nodes of the tree in the following order: left subtree, root, right subtree.

One way to perform inorder traversal is using recursion. We can define a recursive function `inorder` that takes a node as input and performs the following steps:

1. If the node is `None`, return.
2. Call `inorder` on the node's left child.
3. Print the node's data.
4. Call `inorder` on the node's right child.

## Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the tree. This is because each node is visited once.

The space complexity of the inorder traversal is O(h), where h is the height of the tree. This is because the recursion stack can be as deep as the height of the tree.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    """
    Performs inorder traversal on a binary tree.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        None
    """

    # If the root node is None, return.
    if root is None:
        return

    # Call inorder traversal on the left subtree.
    inorder_traversal(root.left)

    # Print the root node's data.
    print(root.data)

    # Call inorder traversal on the right subtree.
    inorder_traversal(root.right)
```

## Example Test Cases

```python
# Test case 1: Empty tree
root = None
inorder_traversal(root)  # Output: None

# Test case 2: Tree with one node
root = TreeNode(1)
inorder_traversal(root)  # Output: 1

# Test case 3: Tree with multiple nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
inorder_traversal(root)  # Output: 2 1 3
```

## Alternative Approaches

There are other ways to perform inorder traversal on a binary tree, such as using a stack or Morris traversal. The stack approach involves storing the nodes of the tree in a stack and visiting them in the following order:

1. Push the root node onto the stack.
2. While the stack is not empty, pop the top node from the stack and print its data.
3. Push the node's right child onto the stack.
4. Push the node's left child onto the stack.

The Morris traversal approach involves modifying the tree to form a circular linked list and then traversing the list to print the node's data.

# Connect with me: https://github.com/ohkrahul
