'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-22
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-22

## 1. Problem Understanding and Approach

The problem asks us to implement inorder traversal of a binary tree. Inorder traversal visits the nodes of a binary tree in the following order: left subtree, root, and right subtree.

Our approach is to use a recursive function to traverse the tree. The function will take a node as input and perform the following steps:
1. if the node is not null,
2. call the function recursively on the left child of the node,
3. visit the node (output its value),
4. call the function recursively on the right child of the node.

## 2. Time and Space Complexity Analysis

The time complexity of our algorithm is O(n), where n is the number of nodes in the tree. This is because we visit each node exactly once.

The space complexity of our algorithm is O(h), where h is the height of the tree. This is because our recursive function can be called at most h times, and each call requires O(1) space for the function call stack.

## 3. Well-commented Implementation

```python
def inorder_traversal(root):
    """
    Perform inorder traversal of a binary tree.

    Parameters:
        root: The root node of the binary tree.

    Returns:
        A list of the values of the nodes in the binary tree, in inorder.
    """

    # If the root is null, return an empty list.
    if root is None:
        return []

    # Recursively traverse the left subtree.
    left_traversal = inorder_traversal(root.left)

    # Visit the root node.
    root_value = root.val

    # Recursively traverse the right subtree.
    right_traversal = inorder_traversal(root.right)

    # Combine the results of the left and right traversals.
    return left_traversal + [root_value] + right_traversal
```

## 4. Example Test Cases

```python
# Test case 1: Empty tree.
root = None
result = inorder_traversal(root)
print(result)  # Output: []

# Test case 2: Single-node tree.
root = TreeNode(1)
result = inorder_traversal(root)
print(result)  # Output: [1]

# Test case 3: Binary tree.
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
result = inorder_traversal(root)
print(result)  # Output: [2, 1, 3]
```

## 5. Alternative Approaches

An alternative approach to inorder traversal is to use a stack. The stack is used to keep track of the nodes that have been visited but not yet output.

The algorithm for inorder traversal using a stack is as follows:

1. Initialize a stack.
2. Push the root node onto the stack.
3. While the stack is not empty,
4. Pop the top node from the stack.
5. Visit the node.
6. Push the right child of the node onto the stack.
7. Push the left child of the node onto the stack.

This algorithm has the same time and space complexity as the recursive algorithm.

# Connect with me: https://github.com/ohkrahul
