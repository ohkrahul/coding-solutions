'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-02-25
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-02-25

## Problem Understanding and Approach

Inorder traversal of a binary tree visits the nodes of the tree in the following order: left subtree, root, right subtree. This traversal order is useful for various applications, including printing the elements of the tree in sorted order.

We will implement the inorder traversal using a recursive approach. The base case of the recursion is when the current node is null. In this case, we simply return. Otherwise, we recursively traverse the left subtree, visit the current node, and then recursively traverse the right subtree.

## Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the tree. This is because we visit each node once. The space complexity is also O(n), as we need to store the nodes in the recursion stack.

## Well-Commented Implementation

```python
def inorder_traversal(root):
    """
    Performs inorder traversal of a binary tree.

    Parameters:
    root: The root node of the binary tree.

    Returns:
    A list of the elements in the binary tree in inorder.
    """

    # Base case: if the root node is null, return an empty list.
    if root is None:
        return []

    # Recursively traverse the left subtree.
    left_subtree = inorder_traversal(root.left)

    # Visit the current node.
    current_node = root.val

    # Recursively traverse the right subtree.
    right_subtree = inorder_traversal(root.right)

    # Return the concatenation of the left subtree, current node, and right subtree.
    return left_subtree + [current_node] + right_subtree
```

## Example Test Cases

```python
# Test case 1: empty tree
root = None
expected_output = []
assert inorder_traversal(root) == expected_output

# Test case 2: tree with one node
root = TreeNode(1)
expected_output = [1]
assert inorder_traversal(root) == expected_output

# Test case 3: tree with multiple nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
expected_output = [2, 1, 3]
assert inorder_traversal(root) == expected_output
```

## Alternative Approaches

There are several alternative approaches to implementing inorder traversal, including:

* **Iterative approach:** This approach uses a stack to store the nodes that have been visited but not yet processed. The algorithm starts at the root node and pushes it onto the stack. Then, it pops the top node from the stack and processes it (visiting it and adding it to the output list). If the popped node has a right child, the right child is pushed onto the stack. The algorithm repeats this process until the stack is empty.
* **Morris traversal:** This approach does not use recursion or a stack. It uses a pointer to traverse the tree and modify the tree structure as it goes. The algorithm starts at the root node and finds the leftmost node in the tree. It then sets the right child of the leftmost node to point to the root node. The algorithm then moves the pointer to the right child of the leftmost node and repeats the process. The algorithm stops when the pointer reaches a node that has no right child. At this point, the tree has been modified so that the inorder traversal can be performed by simply traversing the tree from the root node to the rightmost node.

# Connect with me: https://github.com/ohkrahul
