'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-19
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-19

### 1. Problem Understanding and Approach

Inorder traversal of a binary tree visits nodes in the following order: left subtree, root, right subtree. This is commonly used to print the nodes in sorted order (ascending or descending) if the binary tree is a binary search tree (BST).

To implement inorder traversal, we can use a recursive approach. The base case is when the current node is null. Otherwise, we recursively visit the left subtree, then visit the current node, and finally visit the right subtree.

```python
def inorder_traversal(root):
    # Base case: return when the current node is null
    if root is None:
        return

    # Recursively visit the left subtree
    inorder_traversal(root.left)

    # Visit the current node
    print(root.val)

    # Recursively visit the right subtree
    inorder_traversal(root.right)
```

### 2. Time and Space Complexity Analysis

The time complexity of inorder traversal is O(n), where n is the number of nodes in the binary tree. This is because we visit each node exactly once.

The space complexity is O(h), where h is the height of the binary tree. This is because we need to store the call stack for the recursive function.

### 3. Well-Commented Implementation
```python
# Definition of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    """
    Performs an inorder traversal of a binary tree and prints the values of the nodes.

    :param root: The root node of the binary tree.
    """

    # Base case: return when the current node is null
    if root is None:
        return

    # Recursively visit the left subtree
    inorder_traversal(root.left)

    # Visit the current node
    print(root.val)

    # Recursively visit the right subtree
    inorder_traversal(root.right)
```

### 4. Example Test Cases
```python
# Create a binary tree
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

# Perform inorder traversal
inorder_traversal(tree)

# Output:
# 4
# 2
# 5
# 1
# 3
```

### 5. Alternative Approaches

There are other approaches to implement inorder traversal, such as using an iterative approach. Here is an iterative implementation using a stack:
```python
def inorder_traversal(root):
    # Create a stack and push the root node
    stack = [root]

    # While the stack is not empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # If the node is not null, print its value
        if node is not None:
            print(node.val)

        # Push the right child of the node onto the stack
        stack.append(node.right)

        # Push the left child of the node onto the stack
        stack.append(node.left)
```

# Connect with me: https://github.com/ohkrahul
