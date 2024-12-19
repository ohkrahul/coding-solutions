'''
Problem: Binary Tree Traversal
Platform: LeetCode
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal
Date: 2024-12-19
Author: ohkrahul
---
'''

# Solution by ohkrahul
# Problem from LeetCode - Easy
# Date: 2024-12-19

## Problem Understanding and Approach

**Problem Statement:**
Implement the inorder traversal of a binary tree. Inorder traversal visits the nodes of the tree in the order: left subtree, root, right subtree.

**Approach:**
We can use a recursive approach to traverse the binary tree. The following steps outline our approach:

1. If the root node is null, return (base case).
2. Recursively call the inorder traversal on the left subtree.
3. Visit the root node.
4. Recursively call the inorder traversal on the right subtree.

## Time and Space Complexity Analysis

**Time Complexity:**
O(N), where N is the number of nodes in the tree. We visit each node exactly once during the traversal.

**Space Complexity:**
O(H), where H is the height of the tree. The recursive calls can stack up to a depth equal to the height of the tree.

## Well-Commented Implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: TreeNode):
    """
    Performs inorder traversal of a binary tree and returns the values in an array.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        List[int]: The values of the nodes in inorder.
    """

    # Base case: return if the root is null
    if not root:
        return []

    # Recurse on the left subtree
    left_subtree = inorder_traversal(root.left)

    # Visit the root node
    root_val = [root.val]

    # Recurse on the right subtree
    right_subtree = inorder_traversal(root.right)

    # Combine the results
    return left_subtree + root_val + right_subtree
```

## Example Test Cases

**Example 1:**

```python
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Perform inorder traversal
inorder_result = inorder_traversal(root)

# Print the inorder values
print(inorder_result)  # Output: [4, 2, 5, 1, 3]
```

**Example 2:**

```python
# Create a binary tree
root = TreeNode(1)
root.right = TreeNode(2)

# Perform inorder traversal
inorder_result = inorder_traversal(root)

# Print the inorder values
print(inorder_result)  # Output: [1, 2]
```

## Alternative Approaches

**Iterative Approach:**
Instead of recursion, we can use an iterative approach with a stack. We push the root node onto the stack and while the stack is not empty:

1. Pop the top node from the stack.
2. Visit the node.
3. Push the right child of the node onto the stack.
4. Push the left child of the node onto the stack.

This approach has the same time and space complexity as the recursive approach.

# Connect with me: https://github.com/ohkrahul
