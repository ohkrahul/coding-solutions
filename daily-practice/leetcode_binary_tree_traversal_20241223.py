'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-23
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-23

## Problem Understanding and Approach

**Problem Understanding:**

The inorder traversal of a binary tree involves visiting the nodes in the following order: left subtree, root, right subtree. The goal is to implement a recursive algorithm that traverses the tree and prints the values of the nodes in the inorder sequence.

**Approach:**

* Create a recursive function `inorder` that takes a root node as input.
* If the root node is not `None`, perform the following steps:
    * Call the `inorder` function on the left child of the root.
    * Print the value of the root node.
    * Call the `inorder` function on the right child of the root.

## Time and Space Complexity Analysis

**Time Complexity:** O(N), where N is the number of nodes in the tree. The function visits each node in the tree exactly once.

**Space Complexity:** O(H), where H is the height of the tree. The function uses recursive calls, and the maximum depth of the recursion is equal to the height of the tree.

## Well-commented Implementation

```python
def inorder_traversal(root):
    """
    Performs an inorder traversal of a binary tree.

    Args:
        root: The root node of the tree.

    Returns:
        None. Prints the values of the nodes in the inorder sequence.
    """

    # Base case: if the root is None, return
    if root is None:
        return

    # Recursively traverse the left subtree
    inorder_traversal(root.left)

    # Print the value of the root node
    print(root.val)

    # Recursively traverse the right subtree
    inorder_traversal(root.right)
```

## Example Test Cases

**Test Case 1:**

```
        1
       / \
      2   3
     / \
    4   5
```

**Output:** 4 2 5 1 3

**Test Case 2:**

```
      1
     /
    2
   / \
  3   4
 / \
5   6
```

**Output:** 5 3 6 2 4 1

## Alternative Approaches

**Iterative Approach:**

Instead of using recursion, an iterative approach can be used to perform inorder traversal. This approach uses a stack to keep track of the nodes that need to be visited.

```python
def inorder_traversal_iterative(root):
    stack = []

    while root or stack:
        # While there are nodes in the left subtree, push them onto the stack
        while root:
            stack.append(root)
            root = root.left

        # Pop the top node from the stack and print its value
        root = stack.pop()
        print(root.val)

        # Move to the right subtree
        root = root.right
```

# Connect with me: https://github.com/ohkrahul
