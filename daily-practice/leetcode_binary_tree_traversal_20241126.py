'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-11-26
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-11-26

### Problem Understanding and Approach

Given a binary tree, the inorder traversal visits the nodes in the following order: left subtree, root, right subtree.

To implement inorder traversal, we can use a recursive approach. The function `inorder` takes a node as input and performs the following steps:

1. If the left child of the node is not null, recursively call `inorder` on the left child.
2. Visit the node.
3. If the right child of the node is not null, recursively call `inorder` on the right child.

### Time and Space Complexity Analysis

The time complexity of the inorder traversal is O(n), where n is the number of nodes in the binary tree. This is because each node is visited exactly once.

The space complexity of the inorder traversal is O(h), where h is the height of the binary tree. This is because the recursion stack can be as deep as the height of the tree.

### Well-Commented Implementation

```python
def inorder(root):
    """
    Perform inorder traversal of a binary tree.

    Parameters:
        root: The root node of the binary tree.

    Returns:
        List of values in inorder.
    """

    # If the root is None, return an empty list.
    if root is None:
        return []

    # Recursively call inorder on the left child.
    left_inorder = inorder(root.left)

    # Visit the root.
    root_value = root.val

    # Recursively call inorder on the right child.
    right_inorder = inorder(root.right)

    # Return the concatenation of the left inorder, root value, and right inorder.
    return left_inorder + [root_value] + right_inorder
```

### Example Test Cases

```python
# Example binary tree
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)

# Inorder traversal of the binary tree
inorder(tree) == [4, 2, 5, 1, 3]
```

### Alternative Approaches

There are several alternative approaches to inorder traversal, including:

* **Iterative approach:** This approach uses a stack to keep track of the nodes that have been visited. The algorithm starts by pushing the root node onto the stack. Then, while the stack is not empty, pop the top node from the stack and visit it. If the popped node has a right child, push the right child onto the stack. If the popped node has a left child, push the left child onto the stack.
* **Morris traversal:** This approach does not use a stack or recursion. Instead, it uses a pointer to keep track of the current node. The algorithm starts by setting the pointer to the root node. Then, while the pointer is not null, if the pointer points to a node with no left child, visit the node and move the pointer to the right child. Otherwise, find the inorder predecessor of the current node and set the pointer to the inorder predecessor.

# Connect with me: https://github.com/ohkrahul
