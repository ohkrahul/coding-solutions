'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2025-01-21
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2025-01-21

## Problem Understanding and Approach

In this problem, we are asked to implement the inorder traversal of a binary tree. Inorder traversal refers to visiting the nodes of the tree in the following order: left subtree, root, right subtree.

We can use a recursive approach to implement this traversal. The recursive function will take a node as input and perform the following steps:

1. If the node is not null,
2. invoke the recursive function on the left child of the node,
3. visit the node (print the value of the node),
4. invoke the recursive function on the right child of the node.

## Time and Space Complexity Analysis

The time complexity of the recursive inorder traversal is O(n), where n is the number of nodes in the tree. This is because each node is visited exactly once. The space complexity is also O(n), as the recursive calls require O(n) space for the stack frames.

## Well-commented implementation

```python
def inorder_traversal(root):
    """
    Inorder traversal of a binary tree.

    Args:
        root: The root node of the binary tree.

    Returns:
        A list of the values of the nodes in the tree, in inorder.
    """

    if root is None:
        return []

    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)
```

## Example test cases

```python
assert inorder_traversal(None) == []
assert inorder_traversal(TreeNode(1)) == [1]
assert inorder_traversal(TreeNode(1, TreeNode(2), TreeNode(3))) == [2, 1, 3]
```

## Alternative approaches

An alternative approach to implementing inorder traversal is to use a stack. The stack will store the nodes that have been visited but have not yet been processed. The algorithm will start by pushing the root node onto the stack. Then, while the stack is not empty, the algorithm will pop the top node from the stack, visit it, and push its right child onto the stack. If the node has a left child, the algorithm will push the left child onto the stack. The algorithm will continue until the stack is empty.

The time and space complexity of this approach are both O(n).

# Connect with me: https://github.com/ohkrahul
