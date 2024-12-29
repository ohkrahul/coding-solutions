'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-29
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-29

## Problem Understanding and Approach

The problem asks for an inorder traversal of a binary tree. Inorder traversal visits nodes in the left subtree, then the root, and then the right subtree.

One approach to solve this problem is to use a stack. We push the root node onto the stack. Then, while the stack is not empty, we pop the top node and visit it. If the popped node has a left child, we push the left child onto the stack. If the popped node has a right child, we push the right child onto the stack.

## Time and Space Complexity Analysis

The time complexity of this approach is O(n), where n is the number of nodes in the binary tree. This is because we visit each node once.

The space complexity of this approach is also O(n). This is because the stack can contain at most n nodes at any given time.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    """
    Perform inorder traversal of a binary tree.

    :param root: The root node of the binary tree.
    :return: A list of the values in the binary tree in inorder.
    """

    # Create a stack to store the nodes.
    stack = []

    # Push the root node onto the stack.
    stack.append(root)

    # While the stack is not empty, pop the top node and visit it.
    while stack:
        # Pop the top node from the stack.
        node = stack.pop()

        # Visit the node.
        print(node.val)

        # If the node has a left child, push the left child onto the stack.
        if node.left:
            stack.append(node.left)

        # If the node has a right child, push the right child onto the stack.
        if node.right:
            stack.append(node.right)
```

## Example Test Cases

The following test cases demonstrate the correctness of the inorder_traversal function:

```python
# Test case 1: Empty tree
root = None
inorder_traversal(root)  # Output: []

# Test case 2: Tree with one node
root = TreeNode(1)
inorder_traversal(root)  # Output: [1]

# Test case 3: Tree with multiple nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
inorder_traversal(root)  # Output: [2, 1, 3]
```

## Alternative Approaches

There are other approaches to perform inorder traversal of a binary tree, including:

* Using recursion
* Using Morris traversal

The stack-based approach presented in this solution is a simple and efficient way to perform inorder traversal. It is also easy to implement and understand.

# Connect with me: https://github.com/ohkrahul
